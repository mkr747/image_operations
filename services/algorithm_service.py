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

    def clear(self):
        self.__invoker.clear_commands()

    def add(self, cmd: CommandEnum) -> Command:
        implementation = self.__command_factory.get_command(cmd)
        self.__invoker.add_command(implementation)

        return implementation

    def enable_command(self, uuid: UUID):
        self.__invoker.enable_command(uuid)

    def disable_command(self, uuid: UUID):
        self.__invoker.disable_command(uuid)

    def move(self, uuid: UUID, place: int):
        self.__invoker.move(uuid, place)

    def remove(self, uuid: UUID):
        self.__invoker.remove_command(uuid)

    def load(self, path):
        pass

    def save(self):
        pass
