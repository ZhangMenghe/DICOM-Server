from os import listdir,path
import pydicom
import numpy as np
from pydicom.data import get_testdata_files
from transManager_pb2 import dcmImage
from glob import glob

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

def getVolumeDim(folder_name):
    flist = glob(path.join(folder_name, '*.dcm'))
    ds = pydicom.dcmread(flist[0])
    return ds.Columns, ds.Rows, len(flist)

def getVolumeDimensions(folder_name):
    flist = glob(path.join(folder_name, '*.dcm'))
    ds = pydicom.dcmread(flist[0])
    img_height = ds.Rows
    img_width = ds.Columns
    pos = []
    for f in flist:
        ds = pydicom.dcmread(f)
        posf = 0
        try:
            posf = ds[0x0020,0x1041]
        except KeyError:
            continue
        pos.append(float(posf.value))
    if(len(pos) > 2):
        pos.sort()
        return img_width, img_height, len(flist), abs(pos[0] - pos[-1])
    return img_width, img_height, len(flist), -1
        
