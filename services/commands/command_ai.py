from app.models.enums.command_enum import CommandEnum
from app.services.commands.command import Command


class CommandAI(Command):
    def __init__(self, command: CommandEnum):
        super().__init__(command)
        self.command = self._get_method(command)

    def execute(self, frame):
        return self.command(frame, self.kernel)

    def set_params(self, params: dict) -> None:
        self.kernel = params['kernel']

    def _get_method(self, name):
        switcher = {
            CommandEnum.AI: ''
        }

        return switcher.get(name)
