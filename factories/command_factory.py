from models.enums.command_enum import CommandEnum
from services.commands.command import Command
from services.commands.command_ai import CommandAI
from services.commands.command_morphology import CommandMorphology
from services.commands.command_shape_detection import CommandShapeDetection
from services.commands.command_thresholding import CommandThresholding


class CommandFactory:
    def __init__(self):
        self.commands = {
            CommandEnum.ERODE: (lambda: CommandMorphology(CommandEnum.ERODE)),
            CommandEnum.DILATE: (lambda: CommandMorphology(CommandEnum.DILATE)),
            CommandEnum.OPENING: (lambda: CommandMorphology(CommandEnum.OPENING)),
            CommandEnum.CLOSING: (lambda: CommandMorphology(CommandEnum.CLOSING)),
            CommandEnum.GRADIENT: (lambda: CommandMorphology(CommandEnum.GRADIENT)),
            CommandEnum.SHAPE_DETECTION: (lambda: CommandShapeDetection(CommandEnum.SHAPE_DETECTION)),
            CommandEnum.THRESHOLDING: (lambda: CommandThresholding(CommandEnum.THRESHOLDING)),
            CommandEnum.CHANGE_COLOR_SPACE: (lambda: CommandThresholding(CommandEnum.CHANGE_COLOR_SPACE)),
            CommandEnum.AI_WITH_CONTOURS: (lambda: CommandAI(CommandEnum.AI_WITH_CONTOURS)),
            CommandEnum.DRAW_CONTOURS: (
                lambda: CommandShapeDetection(CommandEnum.DRAW_CONTOURS))
        }

    def get_command(self, command: CommandEnum) -> Command:
        return self.commands[command]()
