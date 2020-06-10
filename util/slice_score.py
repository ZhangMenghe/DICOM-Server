import cv2
import numpy as np

from skimage.util import pad
from skimage.filters import median
from skimage.morphology import square
from scipy.signal import convolve2d as conv2
from skimage.morphology import convex_hull_image

from scipy.stats import norm
from scipy.ndimage.morphology import binary_fill_holes
from scipy.ndimage import maximum_filter, minimum_filter

from util.AnDiffusion import *
from util.hysteresisThresholding import apply_hysteresis_threshold

# global template
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
window = (13, 13)

def mean(F, B, c, f, b):
    return np.nanmean(f)

def rang(F, B, c, f, b):
    return np.ptp(f)

def variance(F, B, c, f, b):
    return np.nanvar(f)

def percent_coefficient_variation(F, B, c, f, b):
    return (np.nanstd(f)/np.nanmean(f))*100

def contrast_per_pixle(F, B, c, f, b):
    filt = np.array([[ -1/8, -1/8, -1/8],[-1/8, 1, -1/8],[ -1/8, -1/8,  -1/8]])
    I_hat = conv2(F, filt, mode='same')
    return np.nanmean(I_hat)

def psnr(img1, img2):
    mse = np.square(np.subtract(img1, img2)).mean()
    return 20 * np.log10(np.nanmax(img1) / np.sqrt(mse))

def fpsnr(F, B, c, f, b):
    I_hat = median(F/np.max(F), square(5))
    return psnr(F, I_hat)

def snr1(F, B, c, f, b):
    return np.nanstd(f) / np.nanstd(b)

def patch(img, patch_size):
    h = int(np.floor(patch_size / 2))
    U = pad(img, pad_width=h, mode='constant')
    [a,b]  = np.where(img == np.max(img))
    a = a[0]
    b = b[0]
    return U[a:a+2*h+1,b:b+2*h+1]

def snr2(F, B, c, f, b):
    fore_patch = patch(F, 5)
    return np.nanmean(fore_patch) / np.nanstd(b)

def snr3(F, B, c, f, b):
    fore_patch = patch(F, 5)
    return np.nanmean(fore_patch)/np.nanstd(fore_patch - np.nanmean(fore_patch))

def snr4(F, B, c, f, b):
    fore_patch = patch(F, 5)
    back_patch = patch(B, 5)
    return np.nanmean(fore_patch) / np.nanstd(back_patch)

def cnr(F, B, c, f, b):
    fore_patch = patch(F, 5)
    back_patch = patch(B, 5)
    return np.nanmean(fore_patch-back_patch) / np.nanstd(back_patch)

def cvp(F, B, c, f, b):
    fore_patch = patch(F, 5)
    return np.nanstd(fore_patch) / np.nanmean(fore_patch)

def cjv(F, B, c, f, b):
    return (np.nanstd(f) + np.nanstd(b)) / abs(np.nanmean(f) - np.nanmean(b))

def efc(F, B, c, f, b):
    n_vox = F.shape[0] * F.shape[1]
    efc_max = 1.0 * n_vox * (1.0 / np.sqrt(n_vox)) * \
        np.log(1.0 / np.sqrt(n_vox))
    cc = (F**2).sum()
    b_max = np.sqrt(abs(cc))
    return float((1.0 / abs(efc_max)) * np.sum(
        (F / b_max) * np.log((F + 1e16) / b_max)))

def fber(F, B, c, f, b):
    fg_mu = np.nanmedian(np.abs(f) ** 2)
    bg_mu = np.nanmedian(np.abs(b) ** 2)
    if bg_mu < 1.0e-3:
        return 0
    return float(fg_mu / bg_mu)

def fb_ratio(F, B, c, f, b):
    return len(f)/len(b)

def moment(F, B, c, f, b):
    # contrast feature img
    maximg = maximum_filter(F, size = window)
    minimg = minimum_filter(F, size = window)
    contrast_img = maximg - minimg
    # image moment
    Fscale_moment = cv2.moments(F)['nu20']
    contrast_moment = cv2.moments(contrast_img)['nu20']
    # binary image
    fgmg = (F > Fscale_moment).astype(np.int)
    fcmg = (F > contrast_moment).astype(np.int)
    fcmc = (contrast_img > contrast_moment).astype(np.int)
    fgmc = (contrast_img > Fscale_moment).astype(np.int)
     # luminance contrast quality score
    q11 = fcmg & fgmg
    q1 = np.sum(c * q11) / max(np.sum(fcmg), np.sum(fgmg)) if max(np.sum(fcmg), np.sum(fgmg)) != 0 else 0

    # texture score
    q22 = fgmc & fcmc
    q2 = np.sum(c * q22) / max(np.sum(fgmc), np.sum(fgmg)) if max(np.sum(fgmc), np.sum(fgmg)) != 0 else 0

    # texture contrast quality score
    q33 = fgmc & fcmc
    q3 = np.sum(c * q33) / np.sum(c) if np.sum(c) != 0 else 0

    # lightness quality score
    q44 = fcmg & fgmg
    q4 = np.sum(c * q44) / np.sum(c) if np.sum(c) != 0 else 0

    # print(f"{q1},{q2},{q3},{q4}")
    # weight
    w1 = w2 = w4 = 0.1
    w3 = 0.7
    Q = w1 * q1 + w2 * q2 + w3 * q3 + w4 * q4
    return Q
    
def exceed_penalty(F,B,c,f,b):
    PW = 2
    chull = convex_hull_image(c)
    (rows, cols) = chull.shape
    wrong_pix_num = np.sum(chull[:PW, :]==1) + np.sum(chull[rows-PW:, :]==1) + np.sum(chull[PW:rows-PW,:PW] == 1) + np.sum(chull[PW:rows-PW,cols-PW:] == 1)
    overall = PW * rows * 2+  PW * cols*2 - 4*PW*PW
    return (1.0 - wrong_pix_num/overall)


measure_func={
        'Mean': mean,
        'Range': rang,
        'Variance': variance, 
        'CV': percent_coefficient_variation,
        'CPP': contrast_per_pixle,
        'PSNR': fpsnr,
        'SNR1': snr1,
        'SNR2': snr2,
        'SNR3': snr3,
        'SNR4': snr4,
        'CNR': cnr,
        'CVP': cvp,
        'CJV': cjv,
        'EFC': efc,
        'FBER': fber,
        'FBRATIO':fb_ratio,
        'MOMENT':moment,
        'EXCEED':exceed_penalty,
}

'''
Function: Pre-process a single image before evaluation
Input: image with 12 bit 
'''
def getPreprocessImage(img_12bit):
    img_8bit = img_12bit * 0.06227106227106227
    ori_img = img_8bit.astype(np.uint8)
    img = cv2.equalizeHist(ori_img)

    diffusion = anisodiff(img,20,50,0.1)
    mu,sigma = norm.fit(diffusion)
    htr = apply_hysteresis_threshold(diffusion,mu,sigma).astype(int)
    pmask = binary_fill_holes(htr)
    mask = cv2.morphologyEx(pmask.astype(np.uint8), cv2.MORPH_CLOSE, kernel)
    if (np.sum(mask) / (mask.shape[0] * mask.shape[1]) < 0.2):
        return []
    fore_image = mask * ori_img
    back_image = (1 - mask) * ori_img
    mask_bool = mask.astype(bool)
    #normalize image
#     F = cv2.normalize(fore_image, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    return [fore_image, back_image, mask, ori_img[mask_bool], img[mask_bool==False]]

'''
Input: image should be of the original value: 12bit
Output: a list of measurements for a single image
'''
def getSingleImageMeasurements(img_12bit, func_lst=[]):
    M = []
    res = getPreprocessImage(img_12bit)
    if len(res) == 0:
        return []
    #unpack res
    [F,B,c,f,b] = res
    if np.std(F) == 0:  # whole zero slice, no measure computing
        return []
    if len(func_lst) == 0:
        func_lst = measure_func.keys()
    for key in func_lst:
        func=measure_func.get(key)
        measure = func(F, B, c, f, b)
        if np.isnan(measure) or np.isinf(measure):
            M.append(0)
        else:
            M.append(measure)
    return M

def gaussian_sampling(rnum, snum):
    mu = int(rnum/2)
    sigma = mu / 3
    sel_ids = np.rint(np.random.normal(mu, sigma, snum))
    return np.sort(sel_ids.astype(np.uint8))

'''
Input: volume 12bit-3D-rawdata, sample_ids from volume, optional function name list
Output: dictionary that contains index and corresponding measurement
'''
def getVolumeScore_Slices(volume_raw, sample_num=-1, sample_ids = [], func_lst=[]):
    Ms = {} 
    if volume_raw.ndim < 3:
        Ms[0] = getSingleImageMeasurements(volume_raw)
        return Ms
    vol_dim = volume_raw.shape[-1]
    
    if len(func_lst) == 0:
        func_lst = measure_func.keys()
    if(len(sample_ids)== 0):    
        if sample_num < 0 or sample_num>vol_dim:
            sample_ids = range(vol_dim)
        else:
            sample_ids = gaussian_sampling(vol_dim, sample_num)
    #volume polution
    MAX_POLLUTED = int(len(sample_ids) / 4)
    polutted_num = 0
    print("sampled:" + str(sample_ids))
    for i in sample_ids:
        if(i<0 or i>=vol_dim):
            continue
        measures =  getSingleImageMeasurements(volume_raw[:,:,i], func_lst)
        if len(measures) == 0:
            if polutted_num > MAX_POLLUTED:
                return {}
            polutted_num+=1
        else:
            Ms[i] = measures
    return Ms