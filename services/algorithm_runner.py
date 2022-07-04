from services.commands.command_invoker import CommandInvoker
from services.dispatchers.frame_dispatcher import FrameDispatcher
from services.image_service import ImageService


class AlgorithmRunner:
    def __init__(self, invoker: CommandInvoker, image_service: ImageService):
        self.__invoker = invoker
        self.__image_service = image_service
        self.__frame_dispatcher = None

    def set_frame_dispatcher(self, frame_dispatcher: FrameDispatcher):
        self.__frame_dispatcher = frame_dispatcher

    def run(self):
        if self.__frame_dispatcher is None:
            return

        while self.__frame_dispatcher.is_opened():
            if not self.__image_service.is_playing():
                continue

            exists, frame = self.__frame_dispatcher.read()
            if not exists:
                break

            output = self.__invoker.execute(frame)
            if not type(output) is list:
                self.__frame_dispatcher.append_output(output)
                self.__image_service.set_current_image(output)
