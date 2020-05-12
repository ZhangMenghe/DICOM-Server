from skimage import data
import SimpleITK as sitk
import numpy as np
from time import sleep
from scipy import ndimage
from skimage import io
import os
from skimage.io import imread

# import each and every file
def filelocation(directory):
    DEBUG =False
    l = []
    for file in os.listdir(directory):
        img = directory + file
        if DEBUG : print (img)
        l.append(img)
    # the os.listdir function do not give the files in the right order 
    #so we need to sort them
    l=sorted(l)
    return l

def org_image(n,l1):
    img_T1 = sitk.ReadImage(l1[n])
    img_T1_255 = sitk.Cast(sitk.RescaleIntensity(img_T1), sitk.sitkUInt8)
    org_nda = sitk.GetArrayFromImage(img_T1_255)
    org_nda=org_nda[0,:,:]
    return img_T1, org_nda


def LoadOrginalImage(l1):
    first = True
    rng        = len(l1)
    img        = []
    cnt        = 0
    w = h = 0
    slice_distance = 0
    slice_thickness = 0
    for i in range(len(l1)):
        item = int(i)
        try:
            # img_T1, org_nda, img_T1_255
            x, y = org_image(item,l1)

            if first:
                # slice thickness property of meta data 
                # '0018|0050'
                slice_distance = x.GetMetaData('0018|0088')
                slice_thickness = x.GetMetaData('0018|0050')
                w, h = y.shape
                first = False
                img = np.zeros((w, h, rng))               #  Read image
            img[:,:,item] = y               #  image array
            cnt+= 1
            sleep(0.01)
        except:
            pass
        
    imgInt = np.zeros((w,h,rng)).astype(np.int64)
    for i in range(cnt):
        imgInt[:,:,i] = img[:,:,i].astype(np.int64)
        
    return (imgInt,cnt, w, h, slice_distance, slice_thickness)
