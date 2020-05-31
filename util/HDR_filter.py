from util.wls_filter import wlsFilter
from util.srs import SRS
from util.virtual_ev import VIG
from util.tonemap import *
import cv2

class HDRFilter:
    def __init__(self, weighted_fusion = True):
        self.weighted_fusion = weighted_fusion
        self.wls = wlsFilter
        self.srs = SRS
        self.vig = VIG
        self.tonemap = tonereproduct

    def process(self, image):
        '''
        :image: MRI grayscale image
        :return: HDR grayscale image
        '''
        rgb_image = 1.0 * cv2.cvtColor(image, cv2.COLOR_GRAY2BGR) / 255

        S = 1.0 * image / np.max(image)
        filtered_nda = self.wls(S)

        L = 1.0*S
        I = filtered_nda
        R = np.log(L+1e-22) - np.log(I+1e-22)
        R_ = self.srs(R, L)
        I_K = self.vig(L, 1.0 - L)
        result_ = 255.0 * self.tonemap(rgb_image, L, R_, I_K, self.weighted_fusion)
        # remember to scale result from (0,1) to (0,255)
        # and then change the data type from float32 to uint8
        result = result_.astype('uint8')
        r = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

        return r
