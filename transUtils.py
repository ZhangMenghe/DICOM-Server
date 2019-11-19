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
        yield datasetInfo(folder_name = folder_name)    

        
def check_or_download_from_outside_server(remote_path, folder):
    if(path.isdir(folder)):
        return True
    if not path.isdir(path.join(remote_path, folder)):
        print("not a dir : "+ path.join(remote_path, folder))
        return False
    # copy from remote_path
    destination = shutil.copytree(path.join(remote_path,folder), path.join(getcwd(),folder))
    print("finish copying to " + destination)
    return True

def parser_folder_config(folder_path):
    if not path.isdir(folder_path):
        print(folder_path + " : Not a path, please double check the name")
        return bundleConfig(file_nums = 0)
    print("folder path: " + folder_path)
    return getBundleConfig(folder_path)

def download_folder_as_stream(folder_path):
    dcm_list=[]
    path_pre=path.join(getcwd(), folder_path)
    for file_path in listdir(folder_path):
        print("file " + file_path)
        dcm_list.append(processDICOM(path.join(path_pre, file_path)))
        dcm_list.sort(key=lambda x: x.position, reverse=False)
    for i in range(len(dcm_list)):
        dcm_list[i].dcmID = i
        yield dcm_list[i]
        # yield processDICOM(cid, path.join(path_pre, file_path))

def save_dcmImgs_to_file(dcm_iterators, out_folder):
    if not path.exists(out_folder):
        makedirs(out_folder)
    for dcm in dcm_iterators:
        with open(path.join(*[getcwd(),out_folder, str(dcm.dcmID)+".dcm"]), 'wb') as f:
            f.write(dcm.data)
        print("write to file id %f, " % dcm.position)
