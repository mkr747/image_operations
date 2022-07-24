from typing import List
from models.enums.widget_enum import WidgetEnum


class ParamsMetadata:
    value: any
    is_readonly: bool
    type: WidgetEnum
    possible_values: List[str]

    def __init__(self, value: any, type: WidgetEnum, possible_values=List[str]):
        self.__value = value
        self.__type = type
        self.__possible_values = possible_values

    @property
    def value(self):
        return self.__value

    @property
    def type(self):
        return self.__width

    @property
    def is_readonly(self):
        return self.__width

    @property
    def possible_values(self):
        return self.__width

    @value.setter
    def value(self, val):
        self.__value = val

    @type.setter
    def type(self, val):
        self.__type = val

    @possible_values.setter
    def possible_values(self, val):
        self.__width = val

    @value.deleter
    def value(self):
        del self.__value

    @type.deleter
    def type(self):
        del self.__type

    @possible_values.deleter
    def possible_values(self):
        del self.__possible_values
