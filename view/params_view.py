from ast import Dict
import string
from uuid import UUID

from app.controllers.algorithm_controller import AlgorithmController
from app.controllers.params_controller import ParamsController
from app.models.params_metadata import ParamsMetadata
from app.tools.gui_builder import GUIBuilder as gb


class ParamsView:
    def __init__(self, algorithmController: AlgorithmController):
        self.__algorithmController = algorithmController
        self.__uuid: UUID
        self.__name: str
        self.__labels = []
        self.__values = []
        self.__params = Dict[str, ParamsMetadata]

    def create(self, window, width=300, height=900):
        self.frame = gb.create_frame(window, width, height)

    def set_params(self, name: string, uuid: UUID, params: Dict[str, ParamsMetadata]):
        self.__params = params
        self.__name = name
        self.__uuid = uuid
        self.__clear()
        for i, key in enumerate(params.keys()):
            self.__labels.append(gb.create_label(self.frame, key, i, 0))
            if(params[key].is_readonly):
                self.__values.append(gb.create_label(self.frame, key, i, 0))
            else:
                self.__values.append(gb.create_entry(self.frame, i, 0))

    def confirm_params(self):
        for i, key in enumerate(self.__params):
            if ~self.__params[key].is_readonly:
                self.__params[key] = self.__values[i].get()

        self.__algorithmController.set_params(self.__uuid, self.__params)

    def __clear(self):
        [label.forget_pack() for label in self.__labels]
        [value.forget_pack() for value in self.__values]
        self.__params = Dict[str, ParamsMetadata]
