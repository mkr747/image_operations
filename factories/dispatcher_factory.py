from cv2 import VideoCapture
from models.resolution import Resolution
from services.dispatchers.frame_dispatcher import FrameDispatcher
from services.dispatchers.image_dispatcher import ImageDispatcher
from services.dispatchers.video_dispatcher import VideoDispatcher


class DispatcherFactory:
    def __init__(self):
        pass

    def create(self, path: str, resolution: Resolution) -> FrameDispatcher:
        path = path[0]
        t = path.split('.')[-1]
        if (t == 'jpg' or t is 'png' or t is 'jpeg'):
            return ImageDispatcher(path, resolution)

        return VideoDispatcher(path, resolution)
