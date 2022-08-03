from typing import Dict, List
from factories.structural_factory import StructuralFactory
from models.parameter_widget import ParameterWidget
from models.enums.widget_enum import WidgetEnum
from models.params_metadata import ParamsMetadata
from models.enums.command_enum import CommandEnum
from services.steps.morphology import Morphology
from .command import Command


class CommandMorphology(Command):
    kernel_type_name = 'Kernel type'
    kernel_n_name = 'Kernel matrix n'
    kernel_m_name = 'Kernel matrix m'

    def __init__(self, command: CommandEnum):
        super().__init__(command)
        self.command = self._get_method(command)
        self.structural_factory = StructuralFactory()

    def execute(self, frame):
        if type(frame) is list:
            return [self.command(f, self.kernel) for f in frame]

        return self.command(frame, self.kernel)

    def set_params(self, params: Dict[str, ParamsMetadata]) -> None:
        kernel = params[self.kernel_type_name][0]
        kernel_m = params[self.kernel_m_name][0]
        kernel_n = params[self.kernel_n_name][0]
        self.kernel = self.structural_factory.get_kernel(
            kernel, kernel_n, kernel_m)

    def is_valid(self) -> bool:
        return self.kernel is not None

    def get_params(self) -> List[ParameterWidget]:
        kernel_type = self.builder_factory.get_widget_builder()
        kernel_type\
            .with_label(self.kernel_type_name)\
            .with_widget(WidgetEnum.COMBOBOX)\
            .with_value('MORPH_RECT')\
            .with_value('MORPH_ELIPSE')\
            .with_value('MORPH_CROSS')\
            .with_value('ONES')

        kernel_m = self.builder_factory.get_widget_builder()
        kernel_m.with_label(self.kernel_m_name).with_widget(WidgetEnum.ENTRY)

        kernel_n = self.builder_factory.get_widget_builder()
        kernel_n.with_label(self.kernel_n_name).with_widget(WidgetEnum.ENTRY)

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
