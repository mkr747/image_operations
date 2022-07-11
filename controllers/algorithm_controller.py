from uuid import UUID
from services.commands.command import Command
from models.enums.command_enum import CommandEnum
from services.algorithm_service import AlgorithmService


class AlgorithmController:
    def __init__(self, algorithmService: AlgorithmService):
        self.__algorithmService = algorithmService

    def clear_algorithm(self):
        self.__algorithmService.clear()

    def add_step(self, cmd: CommandEnum) -> Command:
        return self.__algorithmService.add(cmd)

    def remove_step(self, uuid: UUID):
        self.__algorithmService.remove(uuid)

    def move_step(self, uuid: UUID, place: int):
        self.__algorithmService.move(uuid, place)

    def enable_command(self, uuid: UUID):
        self.__algorithmService.enable_command(uuid)

    def disable_command(self, uuid: UUID):
        self.__algorithmService.disable_command(uuid)

    def load_algorithm(self, path):
        algorithm = self.__algorithmService.load(path)

    def save_algorithm(self):
        self.__algorithmService.save()
