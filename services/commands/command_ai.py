from models.enums.widget_enum import WidgetEnum
from models.params_metadata import ParamsMetadata
from models.enums.command_enum import CommandEnum
from services.commands.command import Command
from services.steps.ai import AI


class CommandAI(Command):
    def __init__(self, command: CommandEnum):
        super().__init__(command)
        self.ai_service = AI()
        self.command = self._get_method(command)
        self.params = {
            'path': ParamsMetadata('', WidgetEnum.ENTRY),
            'labels_path': ParamsMetadata('', WidgetEnum.ENTRY),
            'columns': ParamsMetadata('', WidgetEnum.ENTRY)
        }

    def execute(self, frame):
        return self.command(frame, self.kernel)

    def set_params(self, params: dict[str, ParamsMetadata]) -> None:
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
