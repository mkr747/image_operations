import cv2


class ShapeDetection:
    # jest ich 6
    @staticmethod
    def hu_moment(img):
        im = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        moments = cv2.moments(im)
        huMoments = cv2.HuMoments(moments)

        return huMoments

    @staticmethod
    def is_shape(original_img, expected_img):
        return cv2.matchShapes(original_img, expected_img, cv2.CONTOURS_MATCH_I2, 0)

    @staticmethod
    def moments(img):
        pass


#https://github.com/spmallick/learnopencv/tree/master/HuMoments
