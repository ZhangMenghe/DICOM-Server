from os import listdir,path
import pydicom
import numpy as np
from pydicom.data import get_testdata_files
from transManager_pb2 import dcmImage
from glob import glob
from math import isnan
import cv2
from scipy.stats import norm
from scipy.ndimage import maximum_filter, minimum_filter
from scipy.ndimage.morphology import binary_fill_holes

from util.AnDiffusion import *
from util.hysteresisThresholding import apply_hysteresis_threshold

from collections import namedtuple
dicomStruct = namedtuple("dicomStruct", "raw_data vol_thickness slice_thickness slice_distance")

def processDICOM(file_name, unit_size = 2):
    ds = pydicom.dcmread(file_name)
    if unit_size == 4:
        return dcmImage(dcmID = 0, position = float(ds[0x0020,0x1041].value), data=ds.pixel_array.astype(np.uint32).tobytes())

    return dcmImage(dcmID = 0, position = float(ds[0x0020,0x1041].value), data=ds.pixel_array.tobytes())

def getDICOMData(file_name, unit_size = 2):
    ds = pydicom.dcmread(file_name)
    if unit_size == 4:
        return ds.pixel_array.astype(np.uint32).tobytes()
    return ds.pixel_array.tobytes()
# def getBundleConfig(folder_name):
#     flist = listdir(folder_name)
#     file_name = path.join(folder_name, flist[0])
#     ds = pydicom.dcmread(file_name)
#     return bundleConfig(folder_name = folder_name, file_nums=len(flist), img_width = ds.Columns, img_height=ds.Rows, order_flipped=False)

def getVolume(folder_name):
    flist = glob(path.join(folder_name, '*.dcm'))
    ds = pydicom.dcmread(flist[0])
    volume_data = ds.pixel_array
    if(volume_data.ndim != 2):
        return None
    sd = -1
    st = -1
    try:
        sd = float(ds[0x0018, 0x0088].value)
        st = float(ds[0x0018, 0x0050].value)
    except:
        pass
    
    pos = []
    for f in flist:
        ds = pydicom.dcmread(f)
        posf = 0
        try:
            volume_data = np.dstack((volume_data, ds.pixel_array))
            pos.append(float(ds[0x0020,0x1041].value))
        except KeyError:
            pass
    vt = -1
    if(len(pos) > 2):
        pos.sort()
        vt = abs(pos[0] - pos[-1])
    return dicomStruct(raw_data=volume_data[:,:,1:], vol_thickness=vt, slice_thickness=st, slice_distance=sd)

'''
Input: dicomStruct volume
output: [volume_score, slice_score, total]
'''
def getScore(volume):
    # mask = np.zeros(volume.shape)
    #get volume mask
    vol_dim = volume.raw_data.shape[-1]
    MAX_POLLUTED = int(vol_dim / 4)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
    window = (13, 13)
    scores = []
    polutted_num = 0
    #get volume score
    for i in range(vol_dim):
        img = volume.raw_data[:,:,i]
        diffusion = anisodiff(img,20,50,0.1)
        mu,sigma = norm.fit(diffusion)
        htr = apply_hysteresis_threshold(diffusion,mu,sigma).astype(int)
        pmask = binary_fill_holes(htr)
        mask = cv2.erode(pmask.astype(np.uint16),kernel,iterations = 2)

        if (np.sum(mask) / (mask.shape[0] * mask.shape[1]) < 0.2):
            scores.append(0.0)
            
            if(polutted_num > MAX_POLLUTED):
                break
            polutted_num+=1
            continue
        #normalize image
        gray = cv2.normalize(img, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
        
        # contrast feature img
        maximg = maximum_filter(gray, size = window)
        minimg = minimum_filter(gray, size = window)
        contrast_img = maximg - minimg
        # image moment
        grayscale_moment = cv2.moments(gray)['nu20']
        contrast_moment = cv2.moments(contrast_img)['nu20']
        # binary image
        fgmg = (gray > grayscale_moment).astype(np.int)
        fcmg = (gray > contrast_moment).astype(np.int)
        fcmc = (contrast_img > contrast_moment).astype(np.int)
        fgmc = (contrast_img > grayscale_moment).astype(np.int)
         # luminance contrast quality score
        q11 = fcmg & fgmg
        q1 = np.sum(mask * q11) / max(np.sum(fcmg), np.sum(fgmg)) if max(np.sum(fcmg), np.sum(fgmg)) != 0 else 0

        # texture score
        q22 = fgmc & fcmc
        q2 = np.sum(mask * q22) / max(np.sum(fgmc), np.sum(fgmg)) if max(np.sum(fgmc), np.sum(fgmg)) != 0 else 0

        # texture contrast quality score
        q33 = fgmc & fcmc
        q3 = np.sum(mask * q33) / np.sum(mask) if np.sum(mask) != 0 else 0

        # lightness quality score
        q44 = fcmg & fgmg
        q4 = np.sum(mask * q44) / np.sum(mask) if np.sum(mask) != 0 else 0

        # print(f"{q1},{q2},{q3},{q4}")
        # weight
        w1 = w2 = w4 = 0.1
        w3 = 0.7
        Q = w1 * q1 + w2 * q2 + w3 * q3 + w4 * q4

        if not isnan(Q):
            scores.append(Q)
    score_vol = 0
    score_slice = 0
    if(len(scores) != 0):
        score_vol = sum(scores) / len(scores)
    #slice score
    if(volume.slice_distance > 0 and volume.slice_thickness > 0):
        p = volume.slice_thickness / volume.slice_distance
        # from f(x) = e^(-pi*(x-1)^2)
        score_slice = np.exp(-np.pi * (p - 1)**2)
    num_score = .0
    if(vol_dim > 10):
        num_score+= int(vol_dim/100) * 0.5 + int(vol_dim/50)*0.3 + 0.2
    final_score = score_vol * 0.7 + score_slice * 0.3 + num_score
    return [score_vol, score_slice, final_score]


