import cv2
import numpy as np


class StructuralFactory:
    def __init__(self):
        pass

    def get_kernel(self, type, n, m):
        m = int(m)
        n = int(n)
        kernel = {
            'MORPH_ELIPSE': (lambda: cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (m, n))),
            'MORPH_RECT': (lambda: cv2.getStructuringElement(cv2.MORPH_RECT, (m, n))),
            'MORPH_CROSS': (lambda: cv2.getStructuringElement(cv2.MORPH_CROSS, (m, n))),
            'ONES': (lambda: np.ones(m, n))
        }[type]()

        return kernel

    def get_color_space(self, type):
        color_space = {
            'HLS to RGB': lambda: cv2.COLOR_HLS2BGR,
            'RGB to HLS': lambda: cv2.COLOR_BGR2HLS,
            'HSV to RGB': lambda: cv2.COLOR_HSV2BGR,
            'RGB to HSV': lambda: cv2.COLOR_BGR2HLS,
            'RGB to GRAY': lambda: cv2.COLOR_BGR2GRAY,
            'GRAY to RGB': lambda: cv2.COLOR_GRAY2BGR
        }[type]()

        return color_space
