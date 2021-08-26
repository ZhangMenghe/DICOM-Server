from transManager_pb2 import *
from common_pb2 import *
import sys
#sys.path.append("helmsley")
from dicomUtils import *
from PIL import Image
import numpy as np 
import xlrd
import datetime
import cv2

from generateIndexFile import generateDSIndexFile
from ast import literal_eval

def get_sub_dirs(dir_path):
    dir_names = []
    for fname in listdir(dir_path):
        mpath = path.join(dir_path, fname)
        if path.isdir(mpath):
            dir_names.append(mpath)
    return dir_names

def parse_command():
    import argparse
    parser = argparse.ArgumentParser(description='Dicom-GRPC-Server')
    parser.add_argument('-d', '--pacs_dir', type=str, default='',
                        help = 'path to local dataset')
    parser.add_argument('-f', '--pacs_index_path', type=str, default='',help='path to the pacs file')
    parser.add_argument('-c', '--config_dir', type=str, default='',help='dirctory of config files')
    parser.add_argument('-p', '--port', type=str, default='23333',help='port number')
    args = parser.parse_args()
    return args
'''
Input: path of index file
output: list of volumeStructs built from index file

'''
def build_volume_struct_from_files(rf_path):
    vsc = []
    tn_pre = 'report/' + rf_path.split('/')[-2]
    with open(rf_path, 'r') as rf:
        record_lines = rf.readlines()[3:]
        record_num = int(len(record_lines) / 2)
        for i in range(record_num):
            infos = record_lines[2*i].rstrip('\n').split('/')
            scores_np = np.array(record_lines[2*i+1].split('/')).astype(np.float)
            simg = cv2.imread(path.join(tn_pre, infos[0], 'full.png'), 0)
            if simg is None:
                mdims = literal_eval(infos[1])[:2]
                simg = np.zeros(mdims,dtype=np.uint8)
            spacing = literal_eval(infos[4])
            vsc.append(volumeInfo(folder_name=infos[0], \
                dims = literal_eval(infos[1]),\
                orientation = literal_eval(infos[2]),\
                resolution = [spacing[0],spacing[1], float(infos[5])],\
                volume_loc_range = float(infos[6]),\
                with_mask = infos[-1] in ['True', 'true', '1'],\
                data_source = volumeInfo.DataSource.SERVER,\
                sample_img = simg.tobytes(),\
                scores = scoreInfo(rgroup_id=int(scores_np[0]),\
                        rank_id = int(scores_np[1]),\
                        rank_score = scores_np[2],\
                        raw_score=scores_np[3:-3],\
                        vol_score=scores_np[-3:].tolist())))
    return vsc
class transDataManager():
    def __init__(self, remote_data_path, config_dir, local_data_path = None):
        self.folder_remote_path = remote_data_path
        self.config_dir = config_dir
        self.configs_ = []
        self.config_check_dirty = True
        self.default_sel_percent = 0.8
        self.VR_LEN = 10
        # self.folder_local_path = local_data_path
        # self.dcm_list = []
        # self.unit_size = 2
    
    # def check_or_download_from_outside_server(self, target_folder):
    #     local_folder_path = path.join(self.folder_local_path, target_folder)
    #     if(path.isdir(local_folder_path)):
    #         return True
    #     remote_folder_path = path.join(self.folder_remote_path, target_folder)        
    #     if not path.isdir(remote_folder_path):
    #         return False
    #     # copy from remote_path
    #     destination = shutil.copytree(remote_folder_path, local_folder_path)
    #     print("finish copying to " + destination)
    #     return True
    def get_config_files(self):
        if(self.config_check_dirty):
            self.configs_ = []
            for filename in listdir(self.config_dir):
                if(filename.endswith(".yml") or filename.endswith(".yaml")):
                    with open(path.join(self.config_dir, filename), 'r') as cf:
                        config_info = cf.read()
                        config_name = filename.split('.')[0]
                        self.configs_.append(configResponse.configInfo(file_name=config_name, content=config_info))
            self.config_check_dirty = False
        return configResponse(configs = self.configs_)
    def export_config_file(self, content):
        name = content.splitlines()[0].split(" ")[-1]
        while (name + ".yml") in listdir(self.config_dir):
            name = name + "_c"

        with open(path.join(self.config_dir, name + ".yml"), 'w') as cf:
            cf.write(content)
        self.configs_.append(configResponse.configInfo(file_name=name, content=content))
        return commonResponse(success = True)
    def get_all_available_datasets(self, pacs_index_path):
        if not path.isdir(self.folder_remote_path):
            print("not a dir remote : "+ self.folder_remote_path)
            return
        try:
            workbook = xlrd.open_workbook(pacs_index_path)
        except expression as identifier:
            print("fail to open the workbook")
            return
        
        sheet = workbook.sheet_by_index(0)
        header = sheet.row_values(0)

        #required data    
        try:
            idx_folder = header.index('Directory')
            idx_patient = header.index('Patient Name')
            idx_date = header.index('Scan Date')
            idx_modality = header.index('Modality')
            idx_physician = header.index('Treating Physician')
            idx_mask = header.index('Mask ')
            # idx_folder, idx_patient, idx_date, idx_modality, idx_physician, idx_mask = range(6)
        except ValueError:
            print("Information Lacks")
            return

        dataset_lst = []
        for rowx in range(sheet.nrows-1):
            clist = sheet.row_values(rowx + 1)
            # get modality
            if(clist[idx_modality] not in ['MRI', 'mri', 'CT']):
                continue

            # get date as string
            date_str=""
            if type(clist[idx_date]) == float:
                date_obj = datetime.datetime(*xlrd.xldate_as_tuple(clist[idx_date], workbook.datemode))
                date_str = str(date_obj.date())

            # get volumes that have masks
            volume_with_mask_lst = clist[idx_mask].split('\n')
            if(len(volume_with_mask_lst) and volume_with_mask_lst[0]=="N/A"):
                volume_with_mask_lst = []

            dataset_lst.append(datasetResponse.datasetInfo(folder_name = clist[idx_folder],\
                                            patient_name=clist[idx_patient],\
                                            date=date_str,\
                                            physican_name=clist[idx_physician],\
                                            mask_folders=volume_with_mask_lst))    
        return datasetResponse(datasets = dataset_lst)

    #todo:test this!!!
    def getVolumeInfoListFromDS(self, ds_folder, volume_idxf_name):
        # check dataset exist
        ds_path = path.join(self.folder_remote_path, ds_folder)
        if not path.isdir(ds_path):
            print("Failed to getVolumeInfoListFromDS: dir not exist "+ ds_path)
            return
        # generate or read volume index file
        idx_file_path = path.join(ds_path, volume_idxf_name)
        # if index file not exist, generate it(usually we do this offline)
        if not path.exists(idx_file_path):
            generateDSIndexFile(ds_path, idx_file_path)
        volume_lst = build_volume_struct_from_files(idx_file_path)
        for v in volume_lst:
            if(v.dims[0] > 1000 and v.dims[1]> 1000):
                volume_lst.remove(v)
        group_num = int(len(volume_lst) / self.VR_LEN)
        stream_id = 0
        for i in range(group_num):
            yield volumeResponse(volumes=volume_lst[stream_id:stream_id + self.VR_LEN])
            stream_id+=self.VR_LEN
        if(stream_id != len(volume_lst)):
            yield volumeResponse(volumes = volume_lst[stream_id:])

    def getVolumeInfoListFromDS_old(self, ds_folder, volume_idxf_name):
        # check dataset exist
        ds_path = path.join(self.folder_remote_path, ds_folder)
        if not path.isdir(ds_path):
            print("Failed to getVolumeInfoListFromDS: dir not exist "+ ds_path)
            return
        volume_lst = []
        sort_base_id = []
        # generate or read volume index file
        idx_file_path = path.join(ds_path, volume_idxf_name)
        # if index file not exist, generate it(usually we do this offline)
        if not path.exists(idx_file_path):
            generateDSIndexFile(ds_path, idx_file_path)
        with open(idx_file_path, 'r') as index_file:
            vl_lines = index_file.readlines()
            for line in vl_lines:
                contents = line.split(',')
                has_mask = contents[5] in ('True', 'true', '1')
                volume_lst.append(volumeInfo(folder_name=contents[0],\
                file_nums=int(contents[1]),\
                img_height=int(contents[2]),\
                img_width=int(contents[3]),\
                vol_thickness = float(contents[4]),\
                mask_available = has_mask,\
                quality_score = float(contents[-1])).SerializeToString())
                id_str = contents[0].split('_')[0]
                if(id_str.isnumeric()):
                    sort_base_id.append(int(id_str))
                else:
                    sort_base_id.append(0)
        #order the volume list
        sorted_list = [x for _, x in sorted(zip(sort_base_id,volume_lst), key=lambda pair: pair[0], reverse=False)]
        return volumeResponse(volumes = sorted_list)
    def buildDCMIList_old(self, target_folder):
        # if self.folder_local_path == None:
        #     datapath = path.join(self.folder_remote_path, target_folder)
        # else:
        #     if not self.check_or_download_from_outside_server(target_folder):
        #         return
        #     datapath = path.join(self.folder_local_path, target_folder)
        
        datapath = path.join(self.folder_remote_path, target_folder)
        # self.dcm_list.clear()
        dcm_list = []
        for filename in listdir(datapath):
            #check if dcm image
            if(filename.endswith(".dcm")):
                dcm_list.append(processDICOM(path.join(datapath, filename)))
        
        dcm_list.sort(key=lambda x: x.position, reverse=False)
        return dcm_list
    def buildDCMIList(self, target_folder):
        return processDICOM(glob(path.join(path.join(self.folder_remote_path, target_folder), '*.dcm')))
    def download_folder_as_volume(self, target_folder, unit_size):
        print("downloading..." + target_folder)
        # self.unit_size = unit_size
        dcm_list = processDICOM(glob(path.join(path.join(self.folder_remote_path, target_folder), '*.dcm')))
        print("len:"+str(len(dcm_list)))
        single_chunk_size = len(dcm_list[0].data)
        chunk_limit = 4194304 - single_chunk_size
        
        chunk_data = b""
        chunk_size = 0
        chunk_id = 0
        for dcm in dcm_list:
            # limit for 4M
            if(chunk_size >= chunk_limit):
                chunk_id+=1
                print("Sending the " + str(chunk_id) + " chunk")
                yield volumeWholeResponse(data=chunk_data)
                chunk_data = b""
                chunk_size = 0

            chunk_data += dcm.data
            chunk_size += single_chunk_size
        
        if chunk_size!= 0:
            yield volumeWholeResponse(data=chunk_data)
        print("Finish sending dicom volume of "+target_folder)

    def download_processed_as_volume(self, target_folder):
        print("downloading CLAHE..." + target_folder)
        chunk_limit = 4000000
        chunk_id = 0
        with open(path.join(self.folder_remote_path, target_folder) + '/clahe_data', mode='rb') as file: # b is important -> binary
            fileContent = file.read()
            offset = 0
            for i in range(int(len(fileContent) / chunk_limit)):
                chunk_id+=1
                print("Sending the " + str(chunk_id) + " chunk")
                yield volumeWholeResponse(data=fileContent[offset:offset+chunk_limit])
                offset+=chunk_limit
            if(offset < len(fileContent)):
                yield volumeWholeResponse(data=fileContent[offset:])
            
        print("Finish sending CLAHE dicom volume of "+target_folder)

    def download_folder_as_images(self, target_folder):
        dcm_list = self.buildDCMIList(target_folder)
        for i in range(len(dcm_list)):
            dcm_list[i].dcmID = i
            yield dcm_list[i]
        print("Finish sending images of "+target_folder)

    def get_multi_mask(self, mask_dirs, img_name):
        # if(len(mask_dirs) > 0):
        #TODO: MORE THAN ONE EXTRA INFO for sdir in mask_dirs:
        
        img = np.asarray(Image.open(path.join(mask_dirs[0], img_name)))
        if(img.ndim>2):
            img = img[:,:,0]
        return img.astype(np.uint16) << 8

    def inference_masks_as_volume(self, vl_folder_):
        local_mask_folder = path.join(self.folder_remote_path, vl_folder_, "mask")
        if(path.isdir(local_mask_folder)):
            # load masks and yield all the images
            dirs = get_sub_dirs(local_mask_folder)
            lsize = len(listdir(local_mask_folder)) - len(dirs)

            if(lsize == 0):
                local_mask_folder = dirs.pop(0)
                lsize = len(listdir(local_mask_folder))

            img_name = str(lsize-1) +'.png'
            img = np.asarray(Image.open(path.join(local_mask_folder, img_name)))

            if(img.ndim>2):
                img = img[:,:,0]

            data_u16 = img.astype(np.uint16)
            if(len(dirs) > 0):
                data_u16 += self.get_multi_mask(dirs, img_name)
            
            chunk_data = data_u16.tobytes()
            single_chunk_size = len(chunk_data)
            chunk_size = single_chunk_size
            chunk_limit = 4194304 - single_chunk_size
            chunk_id = 0
            for i in range(1, lsize):
                if(chunk_size >= chunk_limit):
                    chunk_id+=1
                    print("Sending the " + str(chunk_id) + " chunk")
                    yield volumeWholeResponse(data=chunk_data)
                    chunk_data = b""
                    chunk_size = 0

                img_name = str(lsize-i)+ '.png'
                img = np.asarray(Image.open(path.join(local_mask_folder, img_name)))
                if(img.ndim > 2):
                    img = img[:,:,0]
                
                data_u16 = img.astype(np.uint16)
                if(len(dirs) > 0):
                    data_u16 += self.get_multi_mask(dirs, img_name)

                chunk_data += data_u16.tobytes()
                chunk_size += single_chunk_size
            if chunk_size!= 0:
                yield volumeWholeResponse(data=chunk_data)
        print("Finish sending mask volume of "+vl_folder_)                

    def inference_masks_as_images(self, vl_folder_):
        return self.download_folder_as_images(vl_folder_)
    def get_centerline(self, vl_folder):
        cline_file = path.join(self.folder_remote_path, vl_folder, "centerline", "normalized.txt")
        if not path.exists(cline_file):
            return
        with open(cline_file, 'r') as rf:
            contents = rf.readlines()
            record_num = len(contents) % 4000
            for i in range(record_num):
                parts = contents[4000*i+i : 4000*i+i + 4001]
                cd = [.0]*12001
                cd[0] = float(parts[0])
                idx = 1
                for line in parts[1:]:
                    cd[idx:idx+3] = [float(x) for x in line.split(',')]
                    idx+=3
                yield centerlineData(data = cd)
        