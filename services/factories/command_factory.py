from app.models.enums.command_enum import CommandEnum
from app.services.commands.command import Command
from app.services.commands.command_ai import CommandAI
from app.services.commands.command_morphology import CommandMorphology
from app.services.commands.command_shape_detection import CommandShapeDetection
from app.services.commands.command_thresholding import CommandThresholding


class CommandFactory:
    def __init__(self):
        self.commands = {
            CommandEnum.ERODE: CommandMorphology,
            CommandEnum.DILATE: CommandMorphology,
            CommandEnum.OPENING: CommandMorphology,
            CommandEnum.CLOSING: CommandMorphology,
            CommandEnum.GRADIENT: CommandMorphology,
            CommandEnum.SHAPE_DETECTION: CommandShapeDetection,
            CommandEnum.THRESHOLDING: CommandThresholding,
            CommandEnum.CHANGE_COLOR_SPACE: CommandThresholding,
            CommandEnum.AI: CommandAI,
        }

    def get_command(self, command: CommandEnum) -> Command:
        return self.commands[command](command)
