from datetime import date
import logging

from app.tools.time_measurement import TimeMeasure


class Logger:
    def __init__(self):
        self.__logger = logging.getLogger()
        self.__logger.setLevel(logging.DEBUG)
        self.__disabled = False

    def __format(self, text):
        now = date.today()
        return f'{now.strftime("%H:%M:%S")}: {text}'

    def disable(self):
        self.__disabled = True

    def enable(self):
        self.disabled = False

    def log_information(self, text):
        if (self.__disabled):
            return

        self.__logger.info(self.__format(text))
        print(self.__format(text))

    def log_information_from_timer(self, timer: TimeMeasure):
        if (self.__disabled):
            return

        self.__logger.info(self.__format(timer.summary()))

    def log_warning(self, text):
        if (self.__disabled):
            return

        self.__logger.warning(self.__format(text))

    def log_error(self, text):
        if (self.__disabled):
            return

        self.__logger.error(self.__format(text))
