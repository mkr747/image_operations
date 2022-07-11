from ast import Dict
import string
from uuid import UUID
from controllers.params_controller import ParamsController

from models.params_metadata import ParamsMetadata
from factories.gui_factory import GuiFactory as gb


class ParamsView:
    def __init__(self, paramsController: ParamsController):
        self.__params_controller = paramsController
        self.__uuid: UUID
        self.__name: str
        self.__labels = list()
        self.__values = list()
        self.__params = dict

    def create(self, window, width=300, height=900):
        self.__frame = gb.create_frame(window, width, height)

        return self.__frame

    def set_params(self, name: string, uuid: UUID, params: dict[str, ParamsMetadata]):
        self.__params = params
        self.__name = name
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
        print(self.__params.keys())
        self.__name = name
        self.__uuid = uuid
        for i, key in enumerate(self.__params.keys()):
            self.__labels.append(gb.create_label(self.__frame, key, i, 0))
            #if(self.__params[key].is_readonly):
            #    self.__values.append(gb.create_label(self.__frame, key, i, 0))
            #else:
            #    self.__values.append(gb.create_entry(self.__frame, i, 0))
            self.__values.append(gb.create_label(self.__frame, key, i, 0))

    def confirm_params(self):
        for i, key in enumerate(self.__params):
            if ~self.__params[key].is_readonly:
                self.__params[key] = self.__values[i].get()

        self.__params_controller.set_params(self.__uuid, self.__params)

    def __clear(self):
        [label.grid_forget() for label in self.__labels]
        [value.grid_forget() for value in self.__values]
