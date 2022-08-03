from typing import Dict
from models.enums.command_enum import CommandEnum
from models.enums.widget_enum import WidgetEnum
from models.params_metadata import ParamsMetadata
from services.commands.command import Command


class CommandMoments(Command):
    color_space_name = 'Color space from'

    def __init__(self, command: CommandEnum):
        super().__init__(command)
        self.command = self._get_method(command)

    def execute(self, frame):
        if type(frame) is list:
            return [self.command(f) for f in frame]

        return self.command(frame)

    def set_params(self, params: Dict[str, ParamsMetadata]) -> None:
        pass

    def is_valid(self) -> bool:
        return False

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
            CommandEnum.MOMENTS_WITH_CONTOURS: Thresholding.changeColorSpace,
        }

        return switcher.get(name)
