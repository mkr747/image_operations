from app.models.enums.command_enum import CommandEnum
from app.services.image_processing.thresholding import Thresholding
from command import Command


class CommandThresholding(Command):
    def __init__(self, command: CommandEnum):
        super().__init__(command)
        self.command = self._get_method(command)

    def execute(self, frame) -> any:
        if type(frame) is list:
            return [self.command(f, self.thresh) for f in frame]

        return self.command(frame, self.thresh)

    def set_params(self, params: dict) -> None:
        self.thresh = params['thresh']

    def _get_method(self, name):
        switcher = {
            CommandEnum.THRESHOLDING: Thresholding.threshold,
            CommandEnum.CHANGE_COLOR_SPACE: Thresholding.changeColorSpace,
        }

        return switcher.get(name)
