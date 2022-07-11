import string
from uuid import UUID, uuid4

from models.enums.command_enum import CommandEnum


class Command:
    uuid: UUID
    enabled: bool

    def __init__(self, cmd: CommandEnum):
        self.uuid = uuid4()
        self.enabled = True
        self.name = cmd.value[0]
        self.params = dict

    def execute(self) -> None:
        pass

    def disable(self):
        self.enabled = False

    def enable(self):
        self.enable = True

    def set_params(self, params: dict) -> None:
        pass

    def get_params(self) -> dict:
        return self.params

    def get_name(self) -> string:
        return self.name
