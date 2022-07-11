from uuid import UUID
from models.params_metadata import ParamsMetadata
from services.commands.command_invoker import CommandInvoker


class ParamsService:
    def __init__(self, invoker: CommandInvoker):
        self.__invoker = invoker

    def set_params(self, uuid: UUID, params: dict[str, ParamsMetadata]):
        self.__invoker.set_command_params(uuid, params)

    def get_params(self, uuid: UUID) -> dict[str, ParamsMetadata]:
        return self.__invoker.get_command_params(uuid)
