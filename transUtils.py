from os import path, getcwd,listdir, makedirs
import shutil
from transManager_pb2 import *
from dicomUtils import *
from time import sleep
from PIL import Image
import numpy as np 
import glob
import xlrd
import datetime

class transDataManager():
    def __init__(self, remote_data_path, local_data_path):
        # self.rq_foldername = folder_name
        self.folder_remote_path = remote_data_path
        self.folder_local_path = local_data_path# path.join(local_data_path, folder_name)
        self.folder_abs_path = path.join(getcwd(), local_data_path)#, folder_name) 
        self.dcm_list = []
    
    def get_all_available_datasets(self):
        if not path.isdir(self.folder_remote_path):
            print("not a dir remote : "+ self.folder_remote_path)
            return
        # Parse an .xlsx file to get data
        index_file_lst = glob.glob(path.join(self.folder_remote_path, "*.xlsx"))
        if not len(index_file_lst) == 1:
            print("Lack or have multiple index files")
            return
        workbook = xlrd.open_workbook(index_file_lst[0])
        sheet = workbook.sheet_by_index(0)

        header = sheet.row_values(0)
        try:
            idx_folder = header.index('Directory')
            idx_patient = header.index('Patient Name')
            idx_date = header.index('Scan Date')
            idx_default = header.index('Default')
        except ValueError:
            print("Information Lacks")
            return
            # or pass?
        dataset_lst = []
        for rowx in range(sheet.nrows-1):
            clist = sheet.row_values(rowx + 1)
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
            ds_lst.append(volumeResponse.volumeInfo(folder_name=folder, file_nums=dcm_num, img_width= img_width, img_height=img_height, order_flipped=False))
        return volumeResponse(volumes = ds_lst)

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
        
    def download_folder_as_stream(self, target_folder):
        if not self.check_or_download_from_outside_server(target_folder):
            return
        local_folder_path = path.join(self.folder_local_path, target_folder)
        self.dcm_list.clear()
        for file_path in listdir(local_folder_path):
            self.dcm_list.append(processDICOM(path.join(local_folder_path, file_path)))
            self.dcm_list.sort(key=lambda x: x.position, reverse=False)
        for i in range(len(self.dcm_list)):
            self.dcm_list[i].dcmID = i
            yield self.dcm_list[i]

    def inference_masks_as_stream(self, local_mask_path, target_folder):
        local_mask_folder = path.join(local_mask_path, target_folder)
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





