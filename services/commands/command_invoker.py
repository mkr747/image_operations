from typing import List
from uuid import UUID

from models.parameter_widget import ParameterWidget
from models.params_metadata import ParamsMetadata
from .command import Command
import pickle


class CommandInvoker:
    def __init__(self):
        self.__commands = list[Command]()

    def add_command(self, command: Command):
        self.__commands.append(command)

    def remove_command(self, uuid: UUID):
        self.__commands = [cmd for cmd in self.__commands if cmd.uuid != uuid]

    def save_commands(self, path):
        with open(path, 'wb') as output:
            pickle.dump(self.__commands, output, pickle.HIGHEST_PROTOCOL)

    def load_commands(self, path):
        with open(path, 'rb') as input:
            self.__commands = pickle.load(input)

    def set_command_params(self, uuid: UUID, params: dict[str, ParamsMetadata]):
        id = next(i for i, cmd in enumerate(
            self.__commands) if cmd.uuid == uuid)
        self.__commands[id].set_params(params)

    def get_command(self, uuid: UUID):
        return next(cmd for cmd in self.__commands if cmd.uuid == uuid)

    def get_command_params(self, uuid: UUID) -> List[ParameterWidget]:
        id = next(i for i, cmd in enumerate(
            self.__commands) if cmd.uuid == uuid)
        return self.__commands[id].get_params()

    def move(self, uuid: UUID, place: int):
        id = next(i for i, cmd in enumerate(
            self.__commands) if cmd.uuid == uuid)
        self.__commands.insert(place, self.__commands.pop(id))

    def execute(self, frame):
        for cmd in self.__commands:
            if cmd.is_enabled():
                frame = cmd.execute(frame)

        return frame

    def clear_commands(self):
        self.__commands = []

    def length(self):
        return len(self.__commands)

    def __get_id(self, uuid: UUID):
        return next(i for i, step in enumerate(
            self.__stepList) if step[0].uuid == uuid)
