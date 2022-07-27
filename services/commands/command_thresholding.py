from models.enums.widget_enum import WidgetEnum
from models.params_metadata import ParamsMetadata
from models.enums.command_enum import CommandEnum
from models.threshold import Threshold
from services.steps.thresholding import Thresholding
from .command import Command


class CommandThresholding(Command):
    thresh_1_name = '1st threshold'
    thresh_2_name = '2nd threshold'
    thresh_3_name = '3rd threshold'

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
        t11 = params[self.thresh_1_name][0]
        t12 = params[self.thresh_1_name][1]
        t21 = params[self.thresh_1_name][0]
        t22 = params[self.thresh_1_name][1]
        t31 = params[self.thresh_1_name][0]
        t32 = params[self.thresh_1_name][1]
        self.thresh = Threshold(t11=t11, t12=t12, t21=t21,
                                t22=t22, t31=t31, t32=t32)

    def get_params(self) -> dict:
        thresh1 = self.builder_factory.get_widget_builder()
        thresh1.with_label(self.thresh_1_name).with_value(255).with_value(
            255).with_widget(WidgetEnum.SCALE).with_widget(WidgetEnum.SCALE)

        thresh2 = self.builder_factory.get_widget_builder()
        thresh2.with_label(self.thresh_2_name).with_value(255).with_value(
            255).with_widget(WidgetEnum.SCALE).with_widget(WidgetEnum.SCALE)

        thresh3 = self.builder_factory.get_widget_builder()
        thresh3.with_label(self.thresh_3_name).with_value(255).with_value(
            255).with_widget(WidgetEnum.SCALE).with_widget(WidgetEnum.SCALE)

        return [thresh1.build(), thresh2.build(), thresh3.build()]

    def _get_method(self, name):
        switcher = {
            CommandEnum.THRESHOLDING: Thresholding.threshold,
        }

        return switcher.get(name)
