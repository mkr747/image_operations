from models.enums.command_enum import CommandEnum
from services.steps.shape_detection import ShapeDetection
from .command import Command


class CommandShapeDetection(Command):
    def __init__(self, command: CommandEnum):
        super().__init__(command)
        self.command = self._get_method(command)

    def execute(self, frame):
        if type(frame) is list:
            return [self.command(f) for f in frame]

        return self.command(frame)

    def _get_method(self, name):
        switcher = {
            CommandEnum.SHAPE_DETECTION: ShapeDetection.hu_moment,
            CommandEnum.DRAW_CONTOURS: ''
        }

        return switcher.get(name)
