import time


class TimeMeasure:
    def __init__(self, title=''):
        self.__title = title
        self.__start = 0
        self.__stop = 0
        self.__duration = 0
        self.__start_called = False
        self.__stop_called = False

    def has_stopped(self):
        return self.__stop_called

    def has_started(self):
        return self.__start_called

    def start(self):
        self.__start = time.process_time()
        self.__start_called = True

    def stop(self):
        self.__stop = time.process_time()
        self.__stop_called = True

    def duration(self):
        self.__duration = self.__stop - self.__start
        return self.__duration

    def summary(self):
        return f'{self.__title}: {self.__start} - {self.__stop}, duration: {self.__duration}'
