from os import listdir,path
import pydicom
import numpy as np
from pydicom.data import get_testdata_files
from transManager_pb2 import dcmImage

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

def getImageSize(folder_name):
    flist = listdir(folder_name)
    file_name = path.join(folder_name, flist[0])
    ds = pydicom.dcmread(file_name)
    return ds.Columns, ds.Rows