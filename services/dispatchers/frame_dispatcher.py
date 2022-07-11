from abc import ABC, abstractmethod

from models.resolution import Resolution


class FrameDispatcher(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_fps(self) -> int:
        return 0

    @abstractmethod
    def get_resolution(self) -> Resolution:
        return Resolution(0, 0)

    @abstractmethod
    def is_opened(self) -> bool:
        False

    @abstractmethod
    def read(self):
        return (False, None)

    @abstractmethod
    def append_output(self, img) -> None:
        pass

    @abstractmethod
    def save(self, path, sampling, frame_size) -> None:
        pass
