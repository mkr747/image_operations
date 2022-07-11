import cv2


class ShapeDetection:
    # jest ich 6
    @staticmethod
    def hu_moment(img):
        _, im = cv2.threshold(im, 128, 255, cv2.THRESH_BINARY)

        moments = cv2.moments(img)
        huMoments = cv2.HuMoments(moments)

        return huMoments

    @staticmethod
    def is_shape(original_img, expected_img):
        return cv2.matchShapes(original_img, expected_img, cv2.CONTOURS_MATCH_I2, 0)


#https://github.com/spmallick/learnopencv/tree/master/HuMoments
