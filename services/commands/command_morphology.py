from app.models.enums.widget_enum import WidgetEnum
from app.models.params_metadata import ParamsMetadata
from models.enums.command_enum import CommandEnum
from services.steps.morphology import Morphology
from services.steps.shape_detection import ShapeDetection
from services.steps.thresholding import Thresholding
from .command import Command


class CommandMorphology(Command):
    def __init__(self, command: CommandEnum):
        super().__init__(command)
        self.command = self._get_method(command)
        self.params = {
            'kernel': ParamsMetadata('', WidgetEnum.COMBOBOX, ())
        }

    def execute(self, frame):
        if type(frame) is list:
            return [self.command(f, self.kernel) for f in frame]

        return self.command(frame, self.kernel)

    def set_params(self, params: dict(str, ParamsMetadata)) -> None:
        self.kernel = params['kernel']

    def _get_method(self, name):
        switcher = {
            CommandEnum.ERODE: Morphology.erode,
            CommandEnum.DILATE: Morphology.dilate,
            CommandEnum.OPENING: Morphology.opening,
            CommandEnum.CLOSING: Morphology.closing,
            CommandEnum.GRADIENT: Morphology.gradient
        }

        return switcher.get(name)
