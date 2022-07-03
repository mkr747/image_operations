import cv2


class ContourDetection:
    @staticmethod
    def find_contours(img):
        grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        contours, _ = cv2.findContours(
            grey, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_L1)

        return contours
