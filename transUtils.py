from os import path, getcwd, listdir, makedirs
import shutil
from transManager_pb2 import *
from dicomUtils import *
from time import sleep
from PIL import Image
import numpy as np 
import glob
import xlrd
import datetime

def parse_command():
    import argparse
    parser = argparse.ArgumentParser(description='Dicom-GRPC-Server')
    parser.add_argument('-d', '--pacs_dir', type=str, default='',
                        help = 'path to local dataset')
    parser.add_argument('-m', '--pacs_mask_dir', type=str, default='',help='path to all masks')
    parser.add_argument('-f', '--pacs_index_path', type=str, default='',help='path to the pacs file')
    parser.add_argument('-p', '--port', type=str, default='23333',help='port number')
    args = parser.parse_args()
    return args

class transDataManager():
    def __init__(self, remote_data_path, local_data_path = None):
        self.folder_remote_path = remote_data_path
        self.folder_local_path = local_data_path
        self.dcm_list = []
        self.unit_size = 2
    
    def check_or_download_from_outside_server(self, target_folder):
        local_folder_path = path.join(self.folder_local_path, target_folder)
        if(path.isdir(local_folder_path)):
            return True
        remote_folder_path = path.join(self.folder_remote_path, target_folder)        
        if not path.isdir(remote_folder_path):
            return False
        # copy from remote_path
        destination = shutil.copytree(remote_folder_path, local_folder_path)
        print("finish copying to " + destination)
        return True

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
            idx_modality = header.index('Modality')

            idx_default = header.index('Default')
            idx_date = header.index('Scan Date')
        except ValueError:
            print("Information Lacks")
            return

        dataset_lst = []
        for rowx in range(sheet.nrows-1):
            clist = sheet.row_values(rowx + 1)
            # get modality
            if(clist[idx_modality] not in ['MRI', 'mri', 'CT']):
                continue

            # add dataset
            date_str=""
            if type(clist[idx_date]) == float:
                date_obj = datetime.datetime(*xlrd.xldate_as_tuple(clist[idx_date], workbook.datemode))
                date_str = str(date_obj.date())
            dataset_lst.append(datasetResponse.datasetInfo(folder_name = clist[idx_folder],\
                                            patient_name=clist[idx_patient],\
                                            date=date_str,\
                                            default_folder=clist[idx_default]))    
        return datasetResponse(datasets = dataset_lst)

    def get_all_available_volumes(self, target_folder):
        remote_path = path.join(self.folder_remote_path, target_folder)
        if not path.isdir(remote_path):
            print("not a dir remote : "+ remote_path)
            return
        ds_lst = []
        for folder in listdir(remote_path):
            dcm_num = len(glob.glob(path.join(remote_path, folder, '*.dcm')))
            img_width, img_height = getImageSize(path.join(remote_path, folder))
            ds_lst.append(volumeResponse.volumeInfo(folder_name=folder, file_nums=dcm_num, img_width= img_width, img_height=img_height, order_flipped=False, mask_available =False))
        return volumeResponse(volumes = ds_lst)

    def buildDCMIList(self, target_folder):
        if self.folder_local_path == None:
            datapath = path.join(self.folder_remote_path, target_folder)
        else:
            if not self.check_or_download_from_outside_server(target_folder):
                return
            datapath = path.join(self.folder_local_path, target_folder)

        self.dcm_list.clear()
        for file_path in listdir(datapath):
            self.dcm_list.append(processDICOM(path.join(datapath, file_path), self.unit_size))
        
        self.dcm_list.sort(key=lambda x: x.position, reverse=False)

    def download_folder_as_volume(self, target_folder, unit_size):
        self.unit_size = unit_size
        self.buildDCMIList(target_folder)
        single_chunk_size = len(self.dcm_list[0].data)
        chunk_limit = 4194304 - single_chunk_size
        
        chunk_data = b""
        chunk_size = 0
        for dcm in self.dcm_list:
            # limit for 4M
            if(chunk_size >= chunk_limit):
                print("====sending chunk " + str(chunk_size))
                yield volumeWholeResponse(data=chunk_data)
                chunk_data = b""
                chunk_size = 0

            chunk_data += dcm.data
            chunk_size += single_chunk_size
        
        if chunk_size!= 0:
            yield volumeWholeResponse(data=chunk_data)

    def download_folder_as_images(self, target_folder):
        self.buildDCMIList(target_folder)
        for i in range(len(self.dcm_list)):
            self.dcm_list[i].dcmID = i
            yield self.dcm_list[i]

    def inference_masks_as_volume(self, local_mask_path, target_folder):
        local_mask_folder = path.join(local_mask_path, target_folder)
        if(path.isdir(local_mask_folder)):
            # load masks and yield all the images
            lsize = len(listdir(local_mask_folder))
            if lsize != len(self.dcm_list):
                return None
            if(self.unit_size == 2):
                img = np.asarray(Image.open(path.join(local_mask_folder, '0.png')))
                chunk_data = img.astype(np.uint16).tobytes()
                single_chunk_size = len(chunk_data)
                chunk_size = single_chunk_size
                chunk_limit = 4194304 - single_chunk_size
                for i in range(1, lsize):
                    if(chunk_size >= chunk_limit):
                        print("====sending chunk " + str(chunk_size))
                        yield volumeWholeResponse(data=chunk_data)
                        chunk_data = b""
                        chunk_size = 0

                    img = np.asarray(Image.open(path.join(local_mask_folder, str(i)+ '.png')))
                    chunk_data += img.astype(np.uint16).tobytes()
                    chunk_size += single_chunk_size
                if chunk_size!= 0:
                    yield volumeWholeResponse(data=chunk_data)

            # if(self.unit_size == 4):
            #     single_chunk_size = len(self.dcm_list[0].data)
            #     chunk_limit = 4194304 - single_chunk_size
        
            #     chunk_data = b""
            #     chunk_size = 0

            #     for i in range(lsize):
            #         img = np.asarray(Image.open(path.join(local_mask_folder, str(i)+ '.png')))
            #         data = bytearray(img.astype(np.uint16).tobytes())
            #         oridata = bytearray(self.dcm_list[i].data)
            #         idx = 0
            #         while(idx < len(oridata)):
            #             oridata[idx]
                    

    def inference_masks_as_images(self, local_mask_path, target_folder):
        local_mask_folder = path.join(local_mask_path, target_folder)
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





