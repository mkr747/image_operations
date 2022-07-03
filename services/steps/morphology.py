import cv2


class Morphology:
    @staticmethod
    def erode(frame, kernel):
        return cv2.erode(frame, kernel=kernel, borderType=cv2.BORDER_CONSTANT, borderValue=5)

    @staticmethod
    def dilate(frame, kernel):
        return cv2.dilate(frame, kernel=kernel, borderType=cv2.BORDER_CONSTANT, borderValue=5)

    @staticmethod
    def opening(frame, kernel):
        return cv2.morphologyEx(frame, cv2.MORPH_CLOSE, kernel)

    @staticmethod
    def closing(frame, kernel):
        return cv2.morphologyEx(frame, cv2.MORPH_CLOSE, kernel)

    @staticmethod
    def gradient(frame, kernel):
        return cv2.morphologyEx(frame, cv2.MORPH_GRADIENT, kernel)
