from os import listdir,path
import pydicom
import numpy as np
from pydicom.data import get_testdata_files
from transManager_pb2 import dcmImage, bundleConfig

def processDICOM(file_name):
    ds = pydicom.dcmread(file_name)
    print("read dicom : " + file_name)
    return dcmImage(dcmID = 0, position = float(ds[0x0020,0x1041].value), data=ds.pixel_array.astype(np.ubyte).tobytes())

def getBundleConfig(folder_name):
    flist = listdir(folder_name)
    file_name = path.join(folder_name, flist[0])
    ds = pydicom.dcmread(file_name)
    return bundleConfig(folder_name = folder_name, file_nums=len(flist), img_width = ds.Columns, img_height=ds.Rows, order_flipped=False)