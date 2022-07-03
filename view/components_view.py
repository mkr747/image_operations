from app.controllers.algorithm_controller import AlgorithmController
from app.models.enums.command_enum import CommandEnum
from app.factories.gui_factory import GuiFactory as gb


class ComponentView:
    def __init__(self, algorithmService: AlgorithmController):
        self.__algorithmService = algorithmService
        self.__buttons = []

    def create(self, window, width=300, height=900):
        self.frame = gb.create_frame(window, width, height)

        for i, key in enumerate(CommandEnum):
            self.__buttons.append(gb.create_button(
                self.frame, key, self.__algorithmService.add_step(key), i, 0))
