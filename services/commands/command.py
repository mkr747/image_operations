from abc import ABC, abstractmethod
import string
from uuid import UUID

from app.models.enums.command_enum import CommandEnum


class Command(ABC):
    uuid: UUID
    enabled: bool

    @abstractmethod
    def __init__(self, cmd: CommandEnum):
        self.uuid = UUID.uuid4
        self.enabled = True
        self.name = cmd

    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def disable(self):
        self.enabled = False

    @abstractmethod
    def enable(self):
        self.enable = True

    @abstractmethod
    def set_params(self, params: dict) -> None:
        pass

    @abstractmethod
    def get_params(self) -> dict:
        pass

    @abstractmethod
    def get_name(self) -> string:
        return self.name
