from models.enums.command_enum import CommandEnum
from services.commands.command import Command
from services.steps.ai import AI


class CommandAI(Command):
    def __init__(self, command: CommandEnum):
        super().__init__(command)
        self.ai_service = AI()
        self.command = self._get_method(command)

    def execute(self, frame):
        return self.command(frame, self.kernel)

    def set_params(self, params: dict) -> None:
        path = params['path']
        labels_path = params['labels_path']
        column = params['columns']
        self.ai_service.load_model(path)
        self.ai_service.load_labels(labels_path, column)

    def _get_method(self, name):
        switcher = {
            CommandEnum.AI: self.ai_service.predict
        }

        return switcher.get(name)
