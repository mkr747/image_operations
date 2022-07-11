from cv2 import VideoWriter
import cv2
from models.resolution import Resolution

from services.dispatchers.frame_dispatcher import FrameDispatcher


class VideoDispatcher(FrameDispatcher):
    def __init__(self, path: str, resolution: Resolution):
        super().__init__()
        self.__video = cv2.VideoCapture(path)
        self.__video.set(cv2.CAP_PROP_FRAME_WIDTH, resolution.width)
        self.__video.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution.height)
        self.__fps = self.__video.get(cv2.CAP_PROP_FPS)
        self.__output = VideoWriter('output.mp4', cv2.VideoWriter_fourcc(
            'M', 'J', 'P', 'G'), -1, (resolution.width, resolution.height))
        self.__curr_image = []

    def get_fps(self) -> int:
        return self.__fps

    def get_resolution(self) -> Resolution:
        return self.__resolution

    def is_opened(self) -> bool:
        return self.__video.isOpened()

    def read(self):
        exists, self.__curr_image = self.__video.read()
        return exists, self.__curr_image

    def save(self, path, sampling, frame_size) -> None:
        VideoWriter(path, cv2.VideoWriter_fourcc(
            'M', 'J', 'P', 'G'), sampling, frame_size)

    def append_output(self, img):
        self.__output.write(img)

    def __del__(self):
        self.__video.release()
        self.__output.release()
