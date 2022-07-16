from models.enums.widget_enum import WidgetEnum
from models.params_metadata import ParamsMetadata
from services.steps.thresholding import Thresholding
from models.enums.command_enum import CommandEnum
from services.steps.shape_detection import ShapeDetection
from .command import Command


class CommandShapeDetection(Command):
    def __init__(self, command: CommandEnum):
        super().__init__(command)
        self.command = self._get_method(command)
        self.params = {'color_space': ParamsMetadata(
            '', WidgetEnum.COMBOBOX, ('HSL', 'HSV', 'RGB', 'GRAY'))
        }

    def execute(self, frame):
        if type(frame) is list:
            return [self.command(f, self.color_space) for f in frame]

        return self.command(frame, self.color_space)

    def set_params(self, params: dict(str, ParamsMetadata)) -> None:
        self.color_space = params['color_space']

    def _get_method(self, name):
        switcher = {
            CommandEnum.CHANGE_COLOR_SPACE: Thresholding.changeColorSpace,
        }

        return switcher.get(name)
