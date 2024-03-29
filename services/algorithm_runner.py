import cv2
from services.commands.command_invoker import CommandInvoker
from services.dispatchers.frame_dispatcher import FrameDispatcher
from services.image_service import ImageService
import threading


class AlgorithmRunner:
    def __init__(self, invoker: CommandInvoker, image_service: ImageService):
        self.__invoker = invoker
        self.__image_service = image_service
        self.__frame_dispatcher = None

    def set_frame_dispatcher(self, frame_dispatcher: FrameDispatcher):
        self.__frame_dispatcher = frame_dispatcher

    def run(self, is_playing):
        threadLock = threading.Lock()
        if self.__frame_dispatcher is None:
            return

        print('in da runner')
        while self.__frame_dispatcher.is_opened():
            print(is_playing())
            if not is_playing():
                print('break')
                break
            print('proceeding')
            exists, frame = self.__frame_dispatcher.read()
            if not exists:
                print('does not exist')
                break

            if self.__invoker.length() > 0:
                print('executing')
                output = self.__invoker.execute(frame)
            else:
                print('nothing to execute')
                output = frame
            if not type(output) is list:
                self.__frame_dispatcher.append_output(output)
                threadLock.acquire()
                self.__image_service.set_current_image(output)
                threadLock.release()
