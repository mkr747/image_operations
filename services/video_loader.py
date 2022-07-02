from cv2 import VideoWriter
import cv2


class VideoLoader:
    def __init__(self, logger):
        self.logger = logger

    def load(self, path):
        video = cv2.VideoCapture(path)
        fps = video.get(cv2.CAP_PROP_FPS)
        width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)

        return video

    def save(self, path, sampling, frame_size):
        VideoWriter(path, cv2.VideoWriter_fourcc(
            'M', 'J', 'P', 'G'), sampling, frame_size)
