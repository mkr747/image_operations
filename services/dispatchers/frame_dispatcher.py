from abc import ABC

from models.resolution import Resolution


class FrameDispatcher(ABC):
    def __init__(self, path: str, resolution: Resolution):
        super.__init__()
        self.__resolution = resolution

    def get_fps(self) -> int:
        return 0

    def get_resolution(self) -> Resolution:
        return Resolution(0, 0)

    def is_opened(self) -> bool:
        False

    def read(self):
        return (False, None)

    def append_output(self, img) -> None:
        pass

    def save(self, path, sampling, frame_size) -> None:
        pass
