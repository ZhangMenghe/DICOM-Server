from os import path, getcwd,listdir, makedirs
import shutil
from transManager_pb2 import dcmImage, bundleConfig, datasetInfo
from dicomUtils import *
    
def get_all_available_datasets(remote_path):
    if not path.isdir(remote_path):
        print("not a dir : "+ remote_path)
        return
    #todo: parser sth like .csv to get info
    for folder_name in listdir(remote_path):
        yield datasetInfo(folder_name = folder_name,patient_name="Larry Smarr", date="01/01/19", file_nums=48)    

        
def check_or_download_from_outside_server(remote_path, local_path, folder_name):
    local_folder_path = path.join(getcwd(), local_path, folder_name)
    remote_folder_path = path.join(remote_path, folder_name)
    if(path.isdir(local_folder_path)):
        print("====local exist")
        return True
    if not path.isdir(remote_folder_path):
        print("not a dir : "+ remote_folder_path)
        return False
    # copy from remote_path
    destination = shutil.copytree(remote_folder_path, local_folder_path)
    print("finish copying to " + destination)
    return True

def parser_folder_config(local_path, folder_name):
    local_folder_path = path.join(getcwd(), local_path, folder_name)
    if not path.isdir(local_folder_path):
        print(folder_name + " : Not a path, please double check the name")
        return bundleConfig(file_nums = 0)
    print("folder path: " + folder_name)
    return getBundleConfig(local_folder_path)

def download_folder_as_stream(local_path, folder_name):
    dcm_list=[]
    path_pre=path.join(getcwd(), local_path, folder_name)
    print(path_pre)
    for file_path in listdir(path_pre):
        print("file " + file_path)
        dcm_list.append(processDICOM(path.join(path_pre, file_path)))
        dcm_list.sort(key=lambda x: x.position, reverse=False)
    for i in range(len(dcm_list)):
        dcm_list[i].dcmID = i
        yield dcm_list[i]

# def inference_masks_as_stream(local_path, folder_name):


def save_dcmImgs_to_file(dcm_iterators, out_folder):
    if not path.exists(out_folder):
        makedirs(out_folder)
    for dcm in dcm_iterators:
        with open(path.join(*[getcwd(),out_folder, str(dcm.dcmID)+".dcm"]), 'wb') as f:
            f.write(dcm.data)
        print("write to file id %f, " % dcm.position)

class transDataManager():
    def __init__(self):
        self.dcm_list = []
    def download_folder_as_stream(self, local_path, folder_name):
        print("=====")
        self.dcm_list.clear()
        path_pre=path.join(getcwd(), local_path, folder_name)
        for file_path in listdir(path_pre):
            self.dcm_list.append(processDICOM(path.join(path_pre, file_path)))
            self.dcm_list.sort(key=lambda x: x.position, reverse=False)
        for i in range(len(self.dcm_list)):
            self.dcm_list[i].dcmID = i
            yield self.dcm_list[i]
    def inference_masks_as_stream(self):
        for i in range(len(self.dcm_list)):
            print("======inference  %d" % self.dcm_list[i].position)
            yield self.dcm_list[i] 
