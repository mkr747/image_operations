from abc import ABC
import string
import tkinter
from typing import List
from uuid import UUID, uuid4
from models.parameter_widget import ParameterWidget
from factories.builder_factory import BuilderFactory

from models.enums.command_enum import CommandEnum


class Command(ABC):
    uuid: UUID
    enabled: tkinter.BooleanVar

    def __init__(self, cmd: CommandEnum):
        self.uuid = uuid4()
        self.enabled = tkinter.BooleanVar()
        self.name = cmd.value[0]
        self.params = dict
        self.builder_factory = BuilderFactory()

    def execute(self) -> None:
        pass

    def disable(self):
        self.enabled.set(False)

    def enable(self):
        self.enabled.set(True)

    def is_enabled(self):
        return self.enabled.get()

    def set_params(self, params: dict) -> None:
        pass

    def get_params(self) -> List[ParameterWidget]:
        return None

    def get_name(self) -> string:
        return self.name
