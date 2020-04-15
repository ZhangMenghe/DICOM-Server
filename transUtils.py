from os import path, getcwd, listdir, makedirs
import shutil
from transManager_pb2 import *
from dicomUtils import *
from time import sleep
from PIL import Image
import numpy as np 
import xlrd
import datetime

from generateIndexFile import generateDSIndexFile

def parse_command():
    import argparse
    parser = argparse.ArgumentParser(description='Dicom-GRPC-Server')
    parser.add_argument('-d', '--pacs_dir', type=str, default='',
                        help = 'path to local dataset')
    parser.add_argument('-f', '--pacs_index_path', type=str, default='',help='path to the pacs file')
    parser.add_argument('-p', '--port', type=str, default='23333',help='port number')
    args = parser.parse_args()
    return args

class transDataManager():
    def __init__(self, remote_data_path, local_data_path = None):
        self.folder_remote_path = remote_data_path
        # self.folder_local_path = local_data_path
        self.dcm_list = []
        self.unit_size = 2
    
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
            # idx_folder = header.index('Directory')
            # idx_patient = header.index('Patient Name')
            # idx_date = header.index('Scan Date')
            # idx_modality = header.index('Modality')
            # idx_physician = header.index('Treating Physician')
            # idx_mask = header.index('Mask')
            idx_folder, idx_patient, idx_date, idx_modality, idx_physician, idx_mask = range(6)
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

    def getVolumeInfoListFromDS(self, ds_folder, volume_idxf_name):
        # check dataset exist
        ds_path = path.join(self.folder_remote_path, ds_folder)
        if not path.isdir(ds_path):
            print("Failed to getVolumeInfoListFromDS: dir not exist "+ remote_path)
            return
        volume_lst = []
        volume_sort_base_lst = []
        # generate or read volume index file
        idx_file_path = path.join(ds_path, volume_idxf_name)
        # if index file not exist, generate it(usually we do this offline)
        if not path.exists(idx_file_path):
            generateDSIndexFile(ds_path, idx_file_path)
        with open(idx_file_path, 'r') as index_file:
            vl_lines = index_file.readlines()
            for line in vl_lines:
                contents = line.split(',')
                has_mask = contents[4] in ('True', 'true', '1')
                volume_lst.append(volumeResponse.volumeInfo(folder_name=contents[0],\
                file_nums=int(contents[1]),\
                img_width=int(contents[2]),\
                img_height=int(contents[3]),\
                mask_available=has_mask))
                volume_sort_base_lst.append(int(has_mask)*100 + float(contents[5]) + float(contents[6]) + float(contents[7]))
        #order the volume list
        sorted_list = [x for _, x in sorted(zip(volume_sort_base_lst,volume_lst), key=lambda pair: pair[0], reverse=True)]
        # print(volume_sort_base_lst)
        return volumeResponse(volumes = sorted_list)

    def buildDCMIList(self, target_folder):
        # if self.folder_local_path == None:
        #     datapath = path.join(self.folder_remote_path, target_folder)
        # else:
        #     if not self.check_or_download_from_outside_server(target_folder):
        #         return
        #     datapath = path.join(self.folder_local_path, target_folder)
        
        datapath = path.join(self.folder_remote_path, target_folder)
        self.dcm_list.clear()
        for filename in listdir(datapath):
            #check if dcm image
            if(filename.endswith(".dcm")):
                self.dcm_list.append(processDICOM(path.join(datapath, filename), self.unit_size))
        
        self.dcm_list.sort(key=lambda x: x.position, reverse=False)

    def download_folder_as_volume(self, target_folder, unit_size):
        print("downloading..." + target_folder)
        self.unit_size = unit_size
        self.buildDCMIList(target_folder)
        single_chunk_size = len(self.dcm_list[0].data)
        chunk_limit = 4194304 - single_chunk_size
        
        chunk_data = b""
        chunk_size = 0
        chunk_id = 0
        for dcm in self.dcm_list:
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
    

    def download_folder_as_images(self, target_folder):
        self.buildDCMIList(target_folder)
        for i in range(len(self.dcm_list)):
            self.dcm_list[i].dcmID = i
            yield self.dcm_list[i]
        print("Finish sending images of "+target_folder)                

    def inference_masks_as_volume(self, vl_folder_):
        local_mask_folder = path.join(self.folder_remote_path, vl_folder_, "mask")
        if(path.isdir(local_mask_folder)):
            # load masks and yield all the images
            lsize = len(listdir(local_mask_folder))
            if lsize != len(self.dcm_list):
                return None
            if(self.unit_size == 2):
                img = np.asarray(Image.open(path.join(local_mask_folder, str(lsize-1) +'.png')))
                if(img.ndim>2):
                    img = img[:,:,0]
                chunk_data = img.astype(np.uint16).tobytes()
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

                    img = np.asarray(Image.open(path.join(local_mask_folder, str(lsize-i)+ '.png')))
                    if(img.ndim>2):
                        img = img[:,:,0]
                    chunk_data += img.astype(np.uint16).tobytes()
                    chunk_size += single_chunk_size
                if chunk_size!= 0:
                    yield volumeWholeResponse(data=chunk_data)
        print("Finish sending mask volume of "+vl_folder_)                

    def inference_masks_as_images(self, vl_folder_):
        local_mask_folder = path.join(self.folder_remote_path, vl_folder_, "mask")
        print("===="+local_mask_folder)
        if(path.isdir(local_mask_folder)):
            # load masks and yield all the images
            lsize = len(listdir(local_mask_folder))
            if lsize != len(self.dcm_list):
                return None
            for i in range(lsize):
                print("streaming the %d mask" % i)
                # img = plt.imread(path.join(local_mask_folder, str(i)+ '.png'))
                img = np.asarray(Image.open(path.join(local_mask_folder, str(i)+ '.png')))
                #by default, save at the last bit
                yield dcmImage(dcmID = i, position = self.dcm_list[i].position, data=img.astype(np.uint16).tobytes())
        
        else:
            # todo: inference
            # debug: fake~
            lsize = len(self.dcm_list)
            if lsize == 0:
                return None
            # sleep(30)
            for i in range(lsize):
                print("======inference  %d" % self.dcm_list[i].position)
                #todo:save to file
                yield self.dcm_list[i]
        print("Finish sending mask images of "+vl_folder_)





