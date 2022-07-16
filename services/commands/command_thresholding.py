from app.models.enums.widget_enum import WidgetEnum
from app.models.params_metadata import ParamsMetadata
from models.enums.command_enum import CommandEnum
from services.steps.thresholding import Thresholding
from .command import Command


class CommandThresholding(Command):
    def __init__(self, command: CommandEnum):
        super().__init__(command)
        self.command = self._get_method(command)
        self.params = {
            'thresh': ParamsMetadata('', WidgetEnum.LISTBOX)
        }

    def execute(self, frame) -> any:
        if type(frame) is list:
            return [self.command(f, self.thresh) for f in frame]

        return self.command(frame, self.thresh)

    def set_params(self, params: dict) -> None:
        self.thresh = params['thresh']

    def _get_method(self, name):
        switcher = {
            CommandEnum.THRESHOLDING: Thresholding.threshold,
        }

        return switcher.get(name)
