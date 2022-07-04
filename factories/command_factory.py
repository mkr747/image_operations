from models.enums.command_enum import CommandEnum
from services.commands.command import Command
from services.commands.command_ai import CommandAI
from services.commands.command_morphology import CommandMorphology
from services.commands.command_shape_detection import CommandShapeDetection
from services.commands.command_thresholding import CommandThresholding


class CommandFactory:
    def __init__(self):
        self.commands = {
            CommandEnum.ERODE: CommandMorphology(CommandEnum.ERODE),
            CommandEnum.DILATE: CommandMorphology(CommandEnum.DILATE),
            CommandEnum.OPENING: CommandMorphology(CommandEnum.OPENING),
            CommandEnum.CLOSING: CommandMorphology(CommandEnum.CLOSING),
            CommandEnum.GRADIENT: CommandMorphology(CommandEnum.GRADIENT),
            CommandEnum.SHAPE_DETECTION: CommandShapeDetection(CommandEnum.SHAPE_DETECTION),
            CommandEnum.THRESHOLDING: CommandThresholding(CommandEnum.THRESHOLDING),
            CommandEnum.CHANGE_COLOR_SPACE: CommandThresholding(CommandEnum.CHANGE_COLOR_SPACE),
            CommandEnum.AI: CommandAI(CommandEnum.AI),
        }

    def get_command(self, command: CommandEnum) -> Command:
        return self.commands[command]
