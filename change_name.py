import numpy as np 
from PIL import Image
import os

for name in os.listdir('.'):
    num = int(name.split('.')[0][18:])
    os.rename(name, str(num-1)+'.png')