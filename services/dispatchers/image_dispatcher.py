import cv2
from models.resolution import Resolution
from services.dispatchers.frame_dispatcher import FrameDispatcher


class ImageDispatcher(FrameDispatcher):
    def __init__(self, path: str, resolution: Resolution):
        super().__init__()
        self.__image = cv2.resize(cv2.imread(path, cv2.IMREAD_ANYCOLOR), (
            resolution.width, resolution.height), interpolation=cv2.INTER_AREA)
        self.__fps = 1
        self.__curr_image = self.__image

    def get_fps(self) -> int:
        return self.__fps

    def get_resolution(self) -> Resolution:
        return self.__resolution

    def is_opened(self) -> bool:
        return True

    def save(self, path, sampling, frame_size) -> None:
        cv2.imwrite(path, self.__curr_image)

    def append_output(self, img):
        pass

    def __del__(self):
        self.__video.release()
