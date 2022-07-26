from typing import Dict
from factories.structural_factory import StructuralFactory
from models.enums.widget_enum import WidgetEnum
from models.params_metadata import ParamsMetadata
from services.steps.thresholding import Thresholding
from models.enums.command_enum import CommandEnum
from services.steps.shape_detection import ShapeDetection
from .command import Command


class CommandShapeDetection(Command):
    color_space_name = 'Color space from'

    def __init__(self, command: CommandEnum):
        super().__init__(command)
        self.command = self._get_method(command)
        self.structural_factory = StructuralFactory()

    def execute(self, frame):
        if type(frame) is list:
            return [self.command(f, self.color_space) for f in frame]

        return self.command(frame, self.color_space)

    def set_params(self, params: Dict[str, ParamsMetadata]) -> None:
        self.color_space = self.structural_factory.get_color_space(
            params[self.color_space_name][0])

    def get_params(self):
        color_space = self.builder_factory.get_widget_builder()
        color_space\
            .with_label(self.color_space_name)\
            .with_value('HLS to RGB')\
            .with_value('RGB to HLS')\
            .with_value('HSV to RGB')\
            .with_value('RGB to HSV')\
            .with_value('RGB to GRAY')\
            .with_value('GRAY to RGB')\
            .with_widget(WidgetEnum.COMBOBOX)

        return [color_space.build()]

    def _get_method(self, name):
        switcher = {
            CommandEnum.CHANGE_COLOR_SPACE: Thresholding.changeColorSpace,
        }

        return switcher.get(name)
