from ast import Dict
from uuid import UUID
from app.models.enums.command_enum import CommandEnum
from app.models.params_metadata import ParamsMetadata
from app.services.algorithm_service import AlgorithmService
from app.services.commands.command import Command
from app.services.factories.command_factory import CommandFactory
from app.view.algorithm_view import AlgorithmView


class AlgorithmController:
    def __init__(self, algorithmView: AlgorithmView, algorithmService: AlgorithmService):
        self.__algorithmView = algorithmView
        self.__algorithmService = algorithmService

    def clear_algorithm(self):
        self.__algorithmService.clear()

    def add_step(self, cmd: CommandEnum):
        implementation = self.__algorithmService.add(cmd)
        self.__algorithmView.append(implementation)

    def remove_step(self, uuid: UUID):
        self.__algorithmService.remove(uuid)
        self.__algorithmView.remove(uuid)

    def load_algorithm(self, path):
        algorithm = self.__algorithmService.load(path)

    def save_algorithm(self):
        self.__algorithmService.save()

    def set_params(self, uuid: UUID, params: Dict[str, ParamsMetadata]):
        self.__algorithmService.set_params(uuid, params)
