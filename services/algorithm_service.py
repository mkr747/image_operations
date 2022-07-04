from uuid import UUID

from models.enums.command_enum import CommandEnum
from services.commands.command import Command
from services.commands.command_invoker import CommandInvoker
from factories.command_factory import CommandFactory


class AlgorithmService:
    def __init__(self, invoker: CommandInvoker):
        self.__invoker = invoker
        self.__command_factory = CommandFactory()

    def get_step(self, uuid):
        return self.__invoker.get_command(uuid)

    def set_params(self, uuid, params: dict):
        self.__invoker.set_command_params(uuid, params)

    def get_params(self, uuid) -> dict:
        return self.__invoker.get_command_params(uuid)

    def clear(self):
        self.__invoker.clear_commands()

    def add(self, cmd: CommandEnum) -> Command:
        implementation = self.__command_factory.get_command(cmd)
        self.__invoker.add_command(cmd)

        return implementation

    def move(self, uuid: UUID, place: int):
        self.__invoker.move(uuid, place)

    def remove(self, uuid: UUID):
        self.__invoker.remove_command(uuid)

    def load(self, path):
        pass

    def save(self):
        pass
