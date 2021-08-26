from os import path
import pydicom
import numpy as np
from transManager_pb2 import dcmImage
from glob import glob

from util.slice_score import getVolumeScore_Slices

from collections import namedtuple
dicomStruct = namedtuple("dicomStruct", "raw_data meta_data")
default_meta_dic = {
    'volume_dims':[-1,-1,-1], #row, col, slice num
    'img_orientation':[-1,-1,-1,-1,-1,-1], 
    'volume_plane_group':-1,#orientation group, 0 for others, 1, 2, 3 for S,C,T
    'pixel_spacing':[-1,-1],
    'slice_thickness': -1,#type 1C, 
    'volume_loc_range':-1, #from slice_location(type 3)
    'space_between_slices':-1,#type 2
    'mask_available':False
}
default_slice_score_weight = [1.400e-02, 4.000e-03, 0.000e+00, 7.000e-03, 1.510e+01, 4.000e-02,
       2.690e-01, 8.100e-02, 2.700e-02, 2.600e-02, 2.700e-02, 1.152e+00,
       4.000e-03, 4.100e-02, 0.2, 0.2, 1, 1]
default_vol_score_weight = [1.0, 1.0, 5.0]

"""
This function takes IOP of an image and returns its plane (Sagittal, Coronal, Transverse)
1,2,3 FOR S,C,T
0 For otherwise
"""
def getPlaneID(IOP):
    IOP_round = [round(x) for x in IOP]
    plane = np.cross(IOP_round[0:3], IOP_round[3:6])
    plane = [abs(x) for x in plane]
    try:
        return plane.index(1)+1
    except:
        return 0

def processDICOM_old(file_name, unit_size = 2):
    ds = pydicom.dcmread(file_name)
    if unit_size == 4:
        return dcmImage(dcmID = 0, position = float(ds[0x0020,0x1041].value), data=ds.pixel_array.astype(np.uint32).tobytes())

    # return dcmImage(dcmID = 0, position = float(ds[0x0020,0x1041].value), data=ds.pixel_array.tobytes())
    return dcmImage(dcmID = 0, position = ds.InstanceNumber, data=ds.pixel_array.tobytes())

def processDICOM(file_list):
    slices = [pydicom.dcmread(s) for s in file_list]
    slices.sort(key = lambda x: int(x.InstanceNumber))
    images = [s.pixel_array for s in slices]
    return [dcmImage(dcmID=0, position=0, data=img.tobytes()) for img in images]

def getVolume(vol_path):
    location_exist = False
    flist = glob(path.join(vol_path, '*.dcm'))
    #tackle with the first slice
    fs = pydicom.dcmread(flist[0])
    volume_data = fs.pixel_array
    if(volume_data.ndim != 2):
        return None

    #construct meta dic
    meta_dic = dict(default_meta_dic)
    if hasattr(fs, 'ImageOrientationPatient'):
        meta_dic['img_orientation'] = [float(x) for x in fs.ImageOrientationPatient]
        meta_dic['volume_plane_group'] = getPlaneID(fs.ImageOrientationPatient)
    if hasattr(fs, 'PixelSpacing'):
        meta_dic['pixel_spacing'] = [float(x) for x in fs.PixelSpacing]
    if hasattr(fs, 'SliceThickness'):
        meta_dic['slice_thickness'] = float(fs.SliceThickness)
    if hasattr(fs, 'SliceLocation'):
        location_exist = True
    if hasattr(fs, 'SpacingBetweenSlices'):
        meta_dic['space_between_slices'] = float(fs.SpacingBetweenSlices)

    z_locs = []
    instance_id = []
    
    for ipath in flist:
        try:
            ds = pydicom.dcmread(ipath)
        except:
            print("Fail to load " + ipath)
            continue
        
        cvd = ds.pixel_array
        if ds.pixel_array.shape != (fs.Rows, fs.Columns):
            continue
        volume_data = np.dstack((volume_data, ds.pixel_array))
        instance_id.append(ds.InstanceNumber)
        if location_exist:
            z_locs.append(ds.SliceLocation)
    
    volume_data = volume_data[:,:,1:]
    sort_indexes = np.argsort(np.array(instance_id))
    volume_data_sorted = volume_data[:,:,sort_indexes]
    
    if len(z_locs) > 0:
        z_locs_sorted = np.array(z_locs)[sort_indexes]
        meta_dic['volume_loc_range'] = abs(z_locs_sorted[0] - z_locs_sorted[-1])

    dcm_num = volume_data_sorted.shape[-1]
    meta_dic['volume_dims'] = [fs.Rows, fs.Columns, dcm_num]

    vl_mask_path = path.join(vol_path, 'mask')
    if(path.exists(vl_mask_path) and path.isdir(vl_mask_path) and len(glob(vl_mask_path+'/*.png')) == dcm_num):
        meta_dic['mask_available'] = True

    return dicomStruct(raw_data=volume_data_sorted, meta_data = meta_dic)
'''
Input: dicomStruct volume
output: [volume_score, slice_score, total]
'''
def getScore(vd, sample_num = -1, sample_ids = []):
    Ms = getVolumeScore_Slices(vd.raw_data, sample_num, sample_ids)
    slice_scores_avg = np.mean(np.array(list(Ms.values())), axis = 0)
    #sum and weighted sum
    # sum_score = np.sum(slice_scores_avg)
    # weight_avg = np.mean(np.array([x*y for x,y in zip(slice_scores_avg, default_slice_score_weight)]))

    #vol score
    num_score =.0
    vol_dim = vd.meta_data['volume_dims'][-1]
    if( vol_dim > 150):
        num_score = 1.0
    elif(vol_dim > 100):
        num_score = vol_dim / 150.0
    elif(vol_dim > 50):
        num_score = vol_dim / 300.0
        # num_score+= int(vol_dim/100) * 0.5 + int(vol_dim/50)*0.3 + 0.2
    tags_score = .0
    for item in vd.meta_data.values():
        if(isinstance(item, float) and item!=-1):
            tags_score+=1.0
    tags_score = tags_score / 4.0#float([isinstance(x,float) for x in vd.meta_data.values()].count(True))
    mask_score = int(vd.meta_data['mask_available'])
    # vol_score = num_score * default_vol_score_weight[0] + tags_score * default_vol_score_weight[1] + mask_score + default_vol_score_weight[2]
    return [slice_scores_avg, num_score, tags_score, mask_score]



    



