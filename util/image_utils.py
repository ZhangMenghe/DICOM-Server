import numpy as np
def foregroundBackground(mask,originalImage):
    [row,col] = np.shape(mask)
    fg = np.abs(mask*originalImage)
    fg = np.copy(fg)
    bg = originalImage
    bg = np.copy(bg)
    for i in range(row):
        for j in range(col):
                if(mask[i,j]==1):
                    bg[i,j]=255
                if(mask[i,j]==0):
                    fg[i,j]=255
    return (fg,bg)