from PIL import ImageTk, Image

import cv2


class Utils:
    @staticmethod
    def read_iamge(path):
        img = cv2.imread(path)
        return Utils.wrap_image(img)

    @staticmethod
    def wrap_image(img):
        blue, green, red = cv2.split(img)
        img = cv2.merge((red, green, blue))
        im = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=im)

        return imgtk
