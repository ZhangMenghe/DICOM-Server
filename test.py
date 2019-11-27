from transUtils import *

local_data_path = "data"
folder_name = "2016-10-26-series23"
local_mask_path = "data_mask"

manager = transDataManager(local_data_path, folder_name)
itrs1 = manager.download_folder_as_stream()
for dcm in itrs1:
    print(dcm.position)
print("================================")
itrs = manager.inference_masks_as_stream(local_mask_path)

for item in itrs:
    print(item.position)
