from glob import glob
from random import random
import os
import sys
sys.path.append("proto")
from dicomUtils import *
from queue import Queue
import numpy as np
import cv2
import matplotlib.pyplot as plt
from util.slice_score import measure_func

from collections import namedtuple
volumeStruct = namedtuple("volumeStruct", "info_lst cut_group scores_raw scores_vol raw_rank_score")  

def get_vol_info_lst(vol_name, meta_dic):
    res_lst = [vol_name]
    for item in meta_dic.values():
        # if isinstance(item, list):
        #     res_lst = res_lst+item
        # else:
        res_lst.append(item)
    return res_lst

def save_thumbnails(vol_path, raw_data, save_thumb):
    if not os.path.exists(vol_path):
        os.makedirs(vol_path)
    if(save_thumb == 'all'):    
        for i in range(raw_data.shape[-1]):
            tn = cv2.resize(raw_data[:,:,i],None,fx=0.2,fy=0.2)
            plt.imsave(path.join(vol_path, str(i)+'.png'), tn, cmap = 'gray')
    elif(save_thumb == 'full'):
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
'''
Input: info lst
       score lst(should add the ranking id and rank score to the very front)
Output: reordered infolst(should not be changed content, only the order)
        modified and reordered scorelst
'''
def rank_and_reorder(infos, scores):
    #build volumeStruct from inputs
    vsc = []
    for info,score in zip(infos, scores):
        vsc.append(volumeStruct(info_lst=info, cut_group=int(info[3]), scores_raw = np.array(score[:-3]).astype(np.float), scores_vol =np.array(score[-3:]).astype(np.float), raw_rank_score=[]))
    vol_cut_group = []
    for vs in vsc:
        vol_cut_group.append(vs.cut_group)
    unique_group = np.unique(vol_cut_group)
    grouped_vsc = {}
    for gid in unique_group:
        grouped_vsc[gid] = [vs for vs in vsc if vs.cut_group == gid]
    param_num = len(vsc[0].scores_raw) 
    grouped_vsc_sorted = {}
    for gvsc_id in grouped_vsc:
        grouped_vsc_sorted[gvsc_id] = [vs for vs in sorted(grouped_vsc.get(gvsc_id), key=lambda vs: np.mean(vs.scores_raw), reverse=True)]
    default_sel_percent = 0.8
    grouped_vsc_sorted_norm = {}
    for gvsc_id in grouped_vsc:
        gsvsc = grouped_vsc_sorted[gvsc_id]
        max_vs_local = []
        for i in range(param_num):
            max_vs_local.append(np.max([vs.scores_raw[i] for vs in gsvsc]))
        
        for i in range(len(gsvsc)):
            gsvsc[i].raw_rank_score.extend([u/(v+0.0001) for u,v in zip(gsvsc[i].scores_raw,max_vs_local)])
            
        sel_num = int(len(gsvsc) * default_sel_percent)
        sel_gsvc = gsvsc[:sel_num]
        rule_out_gsvc = gsvsc[sel_num:]
        sort_mean_sel_gsvc = [vs for vs in sorted(sel_gsvc, key=lambda vs: np.mean(vs.raw_rank_score)*0.8 + np.mean(vs.scores_vol)*0.2, reverse=True)]
        grouped_vsc_sorted_norm[gvsc_id] = sort_mean_sel_gsvc + rule_out_gsvc

    rinfo_lst = []
    rscore_lst = []
    for gid in unique_group:
        rank=1
        for vs in grouped_vsc_sorted_norm[gid]:
            # vs.rank_score = np.mean(vs.raw_rank_score)
            # vs.rank_id = rank
            rinfo_lst.append(vs.info_lst)
            rscore = np.mean(vs.raw_rank_score)*0.8 + np.mean(vs.scores_vol)*0.2
            rscore_lst.append([gid, rank, rscore] + vs.scores_raw.tolist() + vs.scores_vol.tolist())
            rank+=1
    return rinfo_lst, rscore_lst
def generateDSIndexFile(dspath, sample_num, save_thumb = 'full'):
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

        info_lst = []
        score_lst = []

        for foldername in listdir(dspath):
            folderpath = path.join(dspath, foldername)
            if not path.isdir(folderpath):# or len(listdir(folderpath))<10:
                continue
            vol_names = get_vol_folder_name_lst(dspath, foldername)
            for vol_name in vol_names:
                vol_path = path.join(dspath, vol_name)
                vd = getVolume(vol_path)
                if(len(save_thumb)!=0):
                    save_thumbnails(path.join('report', ds_name, vol_name), vd.raw_data, save_thumb)
                if(vd == None):
                    print("==vd invalid==")
                    continue
                
                num = vd.meta_data['volume_dims'][-1]
                sids = [int(p * num) for p in sids_norm]
                ss, num_score, tags_score, mask_score = getScore(vd, sample_ids = sids)
                info_lst.append(get_vol_info_lst(vol_name, vd.meta_data))
                score_lst.append(ss.tolist() + [num_score, tags_score, mask_score])
        #re-order
        rinfo_lst, rscore_lst = rank_and_reorder(info_lst, score_lst)
        #write contents
        for rinfo,rscore in zip(rinfo_lst, rscore_lst):
            rf.write('/'.join(str(ti) for ti in rinfo) + '\n')
            rf.write('/'.join(str(ti) for ti in rscore)+ '\n')
                
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