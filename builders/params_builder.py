from models.enums.widget_enum import WidgetEnum
from models.parameter_widget import ParameterWidget


class ParamsBuilder:
    def __init__(self):
        self.__param_widget = ParameterWidget()

    def with_value(self, label: str):
        self.__param_widget.values.append(label)

        return self

    def with_static_value(self, label: str):
        self.__param_widget.default = label

        return self

    def with_label(self, label: str):
        self.__param_widget.label = label

        return self

    def with_widget(self, type: WidgetEnum):
        self.__param_widget.types.append(type)

        return self

    def build(self):
        return self.__param_widget
