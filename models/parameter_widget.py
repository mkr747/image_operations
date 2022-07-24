
from tkinter import Frame
from typing import List

from pyparsing import col
from factories.gui_factory import GuiFactory
from models.enums.widget_enum import WidgetEnum


class ParameterWidget:
    types: List[WidgetEnum]
    label: str
    values: list
    is_readonly: bool
    default: str

    def __init__(self):
        self.__factory = GuiFactory()
        self.values = list()
        self.types = list()
        self.default = ''
        self.is_readonly = True
        self.widgets = list()

    def __switch(self, master: Frame, type: WidgetEnum, column: int):
        widget = {
            WidgetEnum.COMBOBOX: (lambda: self.__factory.create_combobox(master, self.values, self.is_readonly, 0, column)),
            WidgetEnum.ENTRY: (lambda: self.__factory.create_entry(master, 0, column)),
            WidgetEnum.SCALE: (lambda: self.__factory.create_scale(master, self.values[column-1], 0, column)),
            WidgetEnum.LABEL: (lambda: self.__factory.create_label(master, self.default, 0, column)),
            WidgetEnum.LISTBOX: (lambda: self.__factory.create_listbox(master, 0, column)),
        }.get(type, None)()

        return widget

    def __create(self, frame: Frame, row: int, column: int):
        self.master = self.__factory.create_frame(
            frame, width=500, height=20)
        self.master.grid()
        self.label_widget = self.__factory.create_label(
            self.master, self.label, row=0, column=0)
        [self.widgets.append(self.__switch(self.master, t, i+1))
         for i, t in enumerate(self.types)]

        return self.label_widget, self.widgets, self.master

    def create(self, frame: Frame, row: int, column: int):
        return self.__create(frame, row, column)
