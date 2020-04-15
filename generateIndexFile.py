from glob import glob
from random import random
from os import path, listdir
from dicomUtils import getImageSize
from queue import Queue
import numpy as np
def debug_score_generator():
    return [random(), random(), random()]

def get_content_str_array(cstr, carray):
    for item in carray:
        if(isinstance(item, list)):
            cstr = get_content_str_array(cstr, item)
        else:
            cstr += str(item) + ","
    return cstr

def get_vol_folder_name_lst(parent_path, foldername):
    res_lst = []
    queue = Queue()
    queue.put(foldername)
    while(queue.qsize()):
        item = queue.get()
        item_path = path.join(parent_path, item)
        if not path.isdir(item_path):
            return res_lst
        #check its children
        subnames = listdir(item_path)
        if(len(subnames) == 0):
            continue
        type_test = [x.endswith('.dcm') for x in subnames]
        #contains both dcm and dirs, check if dir is mask dir, if not ,then it's invalid, ignore
        if(len(np.unique(type_test)) > 1):
            dir_pos = np.where(np.array(type_test) == False)
            dir_pos = dir_pos[0]
            if len(dir_pos)!=1 or subnames[dir_pos[0]]!='mask':
                continue
            res_lst.append(item)
        # contains only dicom files
        elif(type_test[0]):
            res_lst.append(item)
        else:
            [queue.put(path.join(item,name)) for name in subnames]
    return res_lst

# generate an index file for available volumes in a ds
def generateDSIndexFile(dspath, index_file_path):
    if not path.isdir(dspath):
        print("Fail to generateDSIndexFile: dir not exist : "+ dspath)
        return
    with open(index_file_path, "w") as index_file:
        for foldername in listdir(dspath):
            folderpath = path.join(dspath, foldername)
            if not path.isdir(folderpath):
                continue
            vol_names = get_vol_folder_name_lst(dspath, foldername)
            for vol_name in vol_names:
                vol_path = path.join(dspath, vol_name)
                dcm_num = len(glob(path.join(vol_path, '*.dcm')))
                img_width, img_height = getImageSize(vol_path)
                vl_mask_path = path.join(vol_path, 'mask')
                mask_available = path.exists(vl_mask_path) and path.isdir(vl_mask_path) and len(glob(vl_mask_path+'/*.png')) == dcm_num
                # mask_available = path.isdir(mskpath) and path.isdir(path.join(mskpath, folder)) and len(glob(path.join(mskpath, folder, '*.png'))) == dcm_num
                scores = debug_score_generator()
                content = get_content_str_array("", [vol_name, dcm_num, img_height, img_width, mask_available, scores])[:-1]
                content+= "\n"
                # print(content)
                index_file.write(content)
def test_gen():
    root_dir = "/home/eevee/Github/data/PACS/IRB1"
    file_path = "/home/eevee/Github/data/PACS/IRB1/index.txt"
    generateDSIndexFile(root_dir, file_path)
    # generateDSIndexFile(root_dir, "MASKS_", "JH")
def parse_command():
    import argparse
    parser = argparse.ArgumentParser(description='PACS-Generator')
    parser.add_argument('-d', '--pacs_dir', type=str, default='',
                        help = 'path to local dataset')
    args = parser.parse_args()
    return args
def main():
    args = parse_command()
    dsnames = listdir(args.pacs_dir)
    for dsname in dsnames:
        dspath = path.join(args.pacs_dir, dsname)
        if(path.isdir(dspath)):
            print(dspath)
            generateDSIndexFile(dspath, path.join(dspath, "index.txt"))

if __name__ == '__main__':
    main()