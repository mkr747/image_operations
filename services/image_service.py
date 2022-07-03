from numpy import zeros


class ImageService:
    is_video: bool
    is_playing: bool

    def __init__(self, resolution):
        self.__image = zeros(1)
        self.__resolution = resolution
        self.is_video = False
        self.is_playing = False

    def play(self):
        self.is_playing = True

    def stop(self):
        self.is_playing = False

    def get_current_image(self):
        return self.__image

    def set_current_image(self, image):
        self.__image = image

    def load(self, path):
        pass
