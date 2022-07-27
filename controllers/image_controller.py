import threading
from services.algorithm_runner import AlgorithmRunner
from services.image_service import ImageService


class ImageController:
    def __init__(self, imageService: ImageService, algorithmRunner: AlgorithmRunner):
        self.__imageService = imageService
        self.__algorithmRunner = algorithmRunner
        self.__thread = threading.Thread(target=self.__algorithmRunner.run, args=(
            lambda: self.__imageService.is_playing(), ))

    def play(self):
        if(self.__imageService.is_playing()):
            return

        self.__imageService.play()
        self.__thread = threading.Thread(target=self.__algorithmRunner.run, args=(
            lambda: self.__imageService.is_playing(), ))
        self.__thread.start()

    def stop(self):
        self.__imageService.stop()
        self.__thread.join()

    def is_playing(self):
        return self.__imageService.is_playing()

    def get_current_image(self):
        return self.__imageService.get_current_image()

    def load(self, path):
        print('Loaded')
        dispatcher = self.__imageService.load(path)
        self.__algorithmRunner.set_frame_dispatcher(dispatcher)
