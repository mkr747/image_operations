from typing import Sequence
import numpy as np
from models.threshold import Threshold
import cv2


class Thresholding:
    @staticmethod
    def changeColorSpace(img, space):
        return cv2.cvtColor(img, space)

    @staticmethod
    def threshold(img, thresh: Threshold):
        height = img.shape[0]
        width = img.shape[1]
        mask = np.zeros((height, width, 1))
        masks = []
        masks.append(cv2.inRange(img, (thresh.t11, thresh.t21, thresh.t31),
                                 (thresh.t12, thresh.t22, thresh.t32)))
        for m in enumerate(masks):
            mask = cv2.bitwise_or(mask, m)

        return mask

    @staticmethod
    def hsv(img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
