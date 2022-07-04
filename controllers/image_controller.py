from services.image_service import ImageService


class ImageController:
    def __init__(self, imageService: ImageService):
        self.__imageService = imageService

    def play(self):
        self.__imageService.play()

    def stop(self):
        self.__imageService.stop()

    def is_playing(self):
        return self.__imageService.is_playing()

    def get_current_image(self):
        return self.__imageService.get_current_image()

    def load(self, path):
        pass
