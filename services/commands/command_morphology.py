from typing import Dict, List
from models.parameter_widget import ParameterWidget
from models.enums.widget_enum import WidgetEnum
from models.params_metadata import ParamsMetadata
from models.enums.command_enum import CommandEnum
from services.steps.morphology import Morphology
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

    def set_params(self, params: Dict[str, ParamsMetadata]) -> None:
        self.kernel = params['kernel']

    def get_params(self) -> List[ParameterWidget]:
        kernel_type = self.builder_factory.get_widget_builder()
        kernel_type.with_label('Kernel type').with_widget(WidgetEnum.COMBOBOX).with_label('Structure').with_value(
            'MORPH_RECT').with_value('MORPH_ELIPSE').with_value('MORPH_CROSS').with_value('ONES')

        kernel_m = self.builder_factory.get_widget_builder()
        kernel_m.with_label('Kernel matrix m').with_widget(WidgetEnum.ENTRY)

        kernel_n = self.builder_factory.get_widget_builder()
        kernel_n.with_label('Kernel matrix n').with_widget(WidgetEnum.ENTRY)

        return [kernel_type.build(), kernel_m.build(), kernel_n.build()]

    def _get_method(self, name):
        switcher = {
            CommandEnum.ERODE: Morphology.erode,
            CommandEnum.DILATE: Morphology.dilate,
            CommandEnum.OPENING: Morphology.opening,
            CommandEnum.CLOSING: Morphology.closing,
            CommandEnum.GRADIENT: Morphology.gradient
        }

        return switcher.get(name)
