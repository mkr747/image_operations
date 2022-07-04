from controllers.algorithm_controller import AlgorithmController
from models.enums.command_enum import CommandEnum
from factories.gui_factory import GuiFactory as gb


class ComponentView:
    def __init__(self, algorithmController: AlgorithmController):
        self.__algorithmController = algorithmController
        self.__buttons = []

    def create(self, window, width=300, height=900):
        self.__frame = gb.create_frame(window, width, height)

        for i, key in enumerate(CommandEnum):
            self.__buttons.append(gb.create_button(
                self.__frame, key, self.__algorithmController.add_step(key), i, 0))

        return self.__frame
