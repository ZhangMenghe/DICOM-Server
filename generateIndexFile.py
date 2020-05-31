from glob import glob
from random import random
import os
from dicomUtils import *
from queue import Queue
import numpy as np
import cv2
import matplotlib.pyplot as plt
from util.slice_score import measure_func

def get_vol_info_lst(vol_name, meta_dic):
    res_lst = [vol_name]
    for item in meta_dic.values():
        # if isinstance(item, list):
        #     res_lst = res_lst+item
        # else:
        res_lst.append(item)
    return res_lst

def save_thumbnails(vol_path, raw_data):
    if not os.path.exists(vol_path):
        os.makedirs(vol_path)
    for i in range(raw_data.shape[-1]):
        tn = cv2.resize(raw_data[:,:,i],None,fx=0.2,fy=0.2)
        plt.imsave(path.join(vol_path, str(i)+'.png'), tn, cmap = 'gray')
    plt.imsave(path.join(vol_path,'full.png'), raw_data[:,:,int(raw_data.shape[-1]/2)], cmap = 'gray')

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

def generateDSIndexFile(dspath, sample_num, save_thumb = True):
    if(dspath[-1] == '/'):
        dspath = dspath[:-1]
    ds_name = dspath.split('/')[-1]
    
    index_file_path = path.join(dspath, 'index.txt')
    if sample_num == 1:
        sids_norm = [0.5]
    else:
        sids_norm = np.random.normal(0.5, 0.15, sample_num)
    if not path.isdir(dspath):
        print("Fail to generateDSIndexFile: dir not exist : "+ dspath)

    with open(index_file_path, 'w') as rf:
        #write header
        rf.write("#DS Info: name," + ','.join(default_meta_dic.keys()) + '\n')
        rf.write("#score items: " + ','.join(measure_func.keys())+ '\n\n')
        for foldername in listdir(dspath):
            folderpath = path.join(dspath, foldername)
            if not path.isdir(folderpath):# or len(listdir(folderpath))<10:
                continue
            vol_names = get_vol_folder_name_lst(dspath, foldername)
            for vol_name in vol_names:
                vol_path = path.join(dspath, vol_name)
                vd = getVolume(vol_path)
                if(save_thumb):
                    save_thumbnails(path.join('report', ds_name, vol_name), vd.raw_data)
                if(vd == None):
                    print("==vd invalid==")
                    continue
                
                num = vd.meta_data['volume_dims'][-1]
                sids = [int(p * num) for p in sids_norm]
                ss, num_score, tags_score, mask_score = getScore(vd, sample_ids = sids)
                #write contents
                rf.write('/'.join(str(ti) for ti in get_vol_info_lst(vol_name, vd.meta_data)) + '\n')
                scores = ss.tolist() + [num_score, tags_score, mask_score]
                rf.write('/'.join(str(ti) for ti in scores)+ '\n')
                
def parse_command():
    import argparse
    parser = argparse.ArgumentParser(description='PACS-Generator')
    parser.add_argument('-p', '--pacs_dir', type=str, default='',
                        help = 'path to local dataset')
    parser.add_argument('-d', '--dir', type=str, default='',
                        help = 'path to local dataset')
    parser.add_argument('-s', '--samplenum', type=int, default=1,
                        help = 'sampling num')                
    args = parser.parse_args()
    return args
def main():
    args = parse_command()
    if(args.dir):
        generateDSIndexFile(args.dir, args.samplenum)
        return
    dsnames = listdir(args.pacs_dir)
    for dsname in dsnames:
        dspath = path.join(args.pacs_dir, dsname)
        if(path.isdir(dspath)):
            print(dspath)
            generateDSIndexFile(dspath, args.samplenum)

if __name__ == '__main__':
    main()