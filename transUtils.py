from os import path, getcwd,listdir, makedirs
import shutil
from transManager_pb2 import dcmImage, bundleConfig, datasetInfo
from dicomUtils import *
    
def get_all_available_datasets(remote_path):
    if not path.isdir(remote_path):
        print("not a dir remote : "+ remote_path)
        return
    #todo: parser sth like .csv to get info
    for folder_name in listdir(remote_path):
        yield datasetInfo(folder_name = folder_name,patient_name="Larry Smarr", date="01/01/19", file_nums=48)    

def save_dcmImgs_to_file(dcm_iterators, out_folder):
    if not path.exists(out_folder):
        makedirs(out_folder)
    for dcm in dcm_iterators:
        with open(path.join(*[getcwd(),out_folder, str(dcm.dcmID)+".dcm"]), 'wb') as f:
            f.write(dcm.data)
        print("write to file id %f, " % dcm.position)

class transDataManager():
    def __init__(self, local_data_path, folder_name):
        self.rq_foldername = folder_name
        self.rq_folder_local_path = path.join(local_data_path, folder_name)
        self.rq_folder_abs_path = path.join(getcwd(), local_data_path, folder_name) 
        self.dcm_list = []
    def check_or_download_from_outside_server(self, remote_path):
        print("=====")
        remote_folder_path = path.join(remote_path, self.rq_foldername)
        if(path.isdir(self.rq_folder_local_path)):
            print("===return")
            return True
        if not path.isdir(remote_folder_path):
            print("not a dir in remote: "+ remote_folder_path)
            return False
        # copy from remote_path
        destination = shutil.copytree(remote_folder_path, self.rq_folder_local_path)
        print("finish copying to " + destination)
        return True
    def parser_folder_config(self):
        if not path.isdir(self.rq_folder_local_path):
            print(self.rq_folder_local_path + " : Not a path, please double check the name")
            return bundleConfig(file_nums = 0)
        print("folder path: " + self.rq_folder_local_path)
        return getBundleConfig(self.rq_folder_abs_path)
        
    def download_folder_as_stream(self):
        self.dcm_list.clear()
        for file_path in listdir(self.rq_folder_local_path):
            self.dcm_list.append(processDICOM(path.join(self.rq_folder_local_path, file_path)))
            self.dcm_list.sort(key=lambda x: x.position, reverse=False)
        for i in range(len(self.dcm_list)):
            self.dcm_list[i].dcmID = i
            yield self.dcm_list[i]

    def inference_masks_as_stream(self):
        for i in range(len(self.dcm_list)):
            print("======inference  %d" % self.dcm_list[i].position)
            yield self.dcm_list[i] 
