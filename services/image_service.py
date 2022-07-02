class ImageService:
    is_video: bool
    is_playing: bool

    def __init__(self, resolution):
        self.__curr_image
        self.__resolution = resolution
        self.is_video = False
        self.is_playing = False

    def play(self):
        self.is_playing = True

    def stop(self):
        self.is_playing = False

    def load(self, path):
        pass
