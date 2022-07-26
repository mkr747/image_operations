import string
from tkinter import StringVar, ttk
from uuid import UUID
from factories.builder_factory import BuilderFactory
from models.enums.widget_enum import WidgetEnum
from models.parameter_widget import ParameterWidget
from controllers.params_controller import ParamsController

from models.params_metadata import ParamsMetadata
from factories.gui_factory import GuiFactory as gb


class ParamsView:
    def __init__(self, paramsController: ParamsController):
        self.__params_controller = paramsController
        self.__uuid: UUID
        self.__name = list()
        self.__row = list()
        self.__labels = list()
        self.__value_widgets = list()
        self.__values = list()
        self.__params = list()
        self.__builder_factory = BuilderFactory()

    def create(self, window, width=300, height=900):
        self.__frame = gb.create_frame(window, width, height)
        self.__save_button = gb.create_button(
            self.__frame, 'Save', self.confirm_params, 10, 10)
        self.__save_button.grid_forget()


        return self.__frame

    def set_params(self, name: string, uuid: UUID, params: dict[str, ParamsMetadata]):
        self.__params = params
        self.__uuid = uuid
        self.__clear()
        for i, key in enumerate(params.keys()):
            self.__labels.append(gb.create_label(self.__frame, key, i, 0))
            if(params[key].is_readonly):
                self.__values.append(gb.create_label(self.__frame, key, i, 0))
            else:
                self.__values.append(gb.create_entry(self.__frame, i, 0))

    def feed_params(self, uuid, name):
        self.__clear()
        self.__params = self.__params_controller.get_params(uuid)
        self.__uuid = uuid
        self.__name = name
        builder = self.__builder_factory.get_widget_builder()
        label, name_widget, container_name = builder.with_label('Method: ').with_static_value(
            name).with_widget(WidgetEnum.LABEL).build().create(self.__frame, 0, 0)

        self.__row.append(container_name)
        self.__labels.append(label)
        self.__value_widgets.append(name_widget)

        for i, param in enumerate(self.__params):
            label, value_widgets, container = param.create(
                self.__frame, i+1, 0)
            self.__values.append(StringVar())
            self.__row.append(container)
            self.__labels.append(label)
            self.__value_widgets.append(value_widgets)

        self.__save_button.grid(row=10, column=10)

    def confirm_params(self):
        params = dict()
        for i, widget in enumerate(self.__value_widgets):
            values = list()
            for v in widget:
                if(isinstance(v, ttk.Label)):
                    continue

                values.append(v.get())

            params[self.__labels[i].cget("text")] = values

        print(params)
        self.__params_controller.set_params(self.__uuid, params)

    def __clear(self):
        [label.grid_forget() for label in self.__labels]
        [v.grid_forget() for values in self.__value_widgets for v in values]
        [row.grid_forget() for row in self.__row]
        self.__save_button.grid_forget()

        self.__labels = list()
        self.__value_widgets = list()
        self.__row = list()
        self.__name = ''
