from glob import glob
from random import random
from os import path, listdir
from dicomUtils import getImageSize

def debug_score_generator():
    return [random(), random(), random()]

def get_content_str_array(cstr, carray):
    for item in carray:
        if(isinstance(item, list)):
            cstr = get_content_str_array(cstr, item)
        else:
            cstr += str(item) + ","
    return cstr

# generate an index file for available volumes in a ds
def generateDSIndexFile(pacs_root, mask_root_name, dsname):
    dspath = path.join(pacs_root, dsname)
    mskpath = path.join(pacs_root, mask_root_name, dsname)
    if not path.isdir(dspath):
        print("not a dir remote : "+ dspath)
        return
    index_file_name = path.join(dspath, "index.txt")
    with open(index_file_name, "w") as index_file:
        print(dspath)
        for folder in listdir(dspath):
            folder_name = path.join(dspath, folder)
            if not path.isdir(folder_name):
                continue

            dcm_num = len(glob(path.join(folder_name, '*.dcm')))
            img_width, img_height = getImageSize(folder_name)
            mask_available = path.isdir(mskpath) and path.isdir(path.join(mskpath, folder)) and len(glob(path.join(mskpath, folder, '*.png'))) == dcm_num
            scores = debug_score_generator()
            content = get_content_str_array("", [folder, dcm_num, img_height, img_width, mask_available, scores])[:-1]
            content+= "\n"
            print(content)
            index_file.write(content)
def test_gen():
    root_dir = "/home/eevee/Github/data/PACS/"
    generateDSIndexFile(root_dir, "MASKS_", "JH")
        