from numpy import zeros

from factories.dispatcher_factory import DispatcherFactory


class ImageService:
    is_video: bool
    is_playing: bool

    def __init__(self, resolution):
        self.__image = zeros(1)
        self.__resolution = resolution
        self.__is_playing = False
        self.__dispatcherFactory = DispatcherFactory()

    def play(self):
        self.__is_playing = True

    def stop(self):
        self.__is_playing = False

    def is_playing(self):
        return self.__is_playing

    def get_current_image(self):
        return self.__image

    def set_current_image(self, image):
        self.__image = image

    def load(self, path: str):
        return self.__dispatcherFactory.create(path, self.__resolution)
