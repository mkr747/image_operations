from ast import Dict
from uuid import UUID
from app.models.params_metadata import ParamsMetadata
from command import Command
import pickle


class CommandInvoker:
    __commands: list(Command)

    def __init__(self):
        self.__commands = list(Command)

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

    def set_command_params(self, uuid: UUID, params: Dict[str, ParamsMetadata]):
        id = self.__commands.index(lambda step: step.uuid == uuid)
        self.__commands[id].set_params(params)

    def get_command(self, uuid: UUID):
        return self.__commands.filter(lambda cmd: cmd.uuid == uuid)

    def get_command_params(self, uuid: UUID) -> dict:
        id = self.__commands.index(lambda step: step.uuid == uuid)
        return self.__commands[id].get_params()

    def move(self, uuid: UUID, place: int):
        cmd = self.__commands.filter(lambda c: c.uuid == uuid)
        self.__commands.remove(lambda c: c.uuid == uuid)
        self.__commands.insert(place, cmd)

    def disable_command(self, uuid: UUID):
        [cmd.disable() for cmd in self.__commands if cmd.uuid == uuid]

    def enable_command(self, uuid: UUID):
        [cmd.enable() for cmd in self.__commands if cmd.uuid == uuid]

    def execute(self, frame):
        for cmd in self.__commands:
            if cmd.enabled:
                frame = cmd.execute(frame)

        return frame

    def clear_commands(self):
        self.__commands = []
