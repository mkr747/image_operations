
from app.models.enums.command_enum import CommandEnum
from app.services.image_processing.morphology import Morphology
from app.services.image_processing.shape_detection import ShapeDetection
from app.services.image_processing.thresholding import Thresholding
from command import CommandAbstract


class CommandMorphology(CommandAbstract):
    def __init__(self, command: CommandEnum):
        super().__init__(command)
        self.command = self._get_method(command)

    def execute(self, frame):
        if type(frame) is list:
            return [self.command(f, self.kernel) for f in frame]

        return self.command(frame, self.kernel)

    def set_params(self, params: dict) -> None:
        self.kernel = params['kernel']

    def _get_method(self, name):
        switcher = {
            CommandEnum.ERODE: Morphology.erode,
            CommandEnum.DILATE: Morphology.dilate,
            CommandEnum.OPENING: Morphology.opening,
            CommandEnum.CLOSING: Morphology.closing,
            CommandEnum.GRADIENT: Morphology.gradient
        }

        return switcher.get(name)
