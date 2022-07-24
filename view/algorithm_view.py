from functools import partial
from tkinter import PhotoImage
from uuid import UUID
from tools.utils import Utils
from controllers.algorithm_controller import AlgorithmController
from models.enums.command_enum import CommandEnum
from view.params_view import ParamsView

from controllers.runner_controller import RunnerController
from factories.gui_factory import GuiFactory as gf


class AlgorithmView:
    def __init__(self, algorithmController: AlgorithmController, paramsView: ParamsView, runnerController: RunnerController):
        self.__paramsView = paramsView
        self.__runnerController = runnerController
        self.__algorithmController = algorithmController
        self.__stepList = list()

    def create(self, window, width=300, height=900):
        self.__frame = gf.create_frame(window, width, height)
        self.__downIcon = Utils.read_iamge('./assets/down.jpg', 20, 10)
        self.__upIcon = Utils.read_iamge('./assets/up.jpg', 20, 10)
        self.__editIcon = Utils.read_iamge('./assets/edit.png', 10, 10)
        self.__deleteIcon = Utils.read_iamge('./assets/delete.png', 10, 10)
        self.__navigation_frame = gf.create_frame(self.__frame, 0, 0)

        self.__algorithm_frame = gf.create_frame(self.__frame, 0, 0)
        self.__navigation_frame.grid(
            row=0, column=0, sticky="w")
        self.__algorithm_frame.grid(
            row=2, column=0)

        self.__runButton = gf.create_button(
            self.__navigation_frame, 'Run', self.__play, row=1, column=1)

        self.__saveButton = gf.create_button(
            self.__navigation_frame, 'Save', self.__play, row=1, column=2)
        self.__loadButton = gf.create_button(
            self.__navigation_frame, 'Load algorith', self.__play, row=1, column=3)

        return self.__frame

    def append(self, step: CommandEnum):
        cmd = self.__algorithmController.add_step(step)
        row = self.__get_last_item()
        checkbutton = gf.create_checkbox(
            self.__algorithm_frame, cmd.get_name(), column=0, row=row, sticky='w')
        editButton = self.__create_edit_button(
            self.__algorithm_frame, cmd.uuid, row, cmd.name)
        deleteButton = self.__create_delete_button(
            self.__algorithm_frame, cmd.uuid, row)
        moveUpButton = self.__create_move_button(
            self.__algorithm_frame, cmd.uuid, self.__upIcon, row, 1, True)
        moveDownButton = self.__create_move_button(
            self.__algorithm_frame, cmd.uuid, self.__downIcon, row, 2, False)

        self.__stepList.append(
            [cmd.uuid, checkbutton, moveUpButton, moveDownButton, editButton, deleteButton])

    def __get_last_item(self):
        return len(self.__stepList)+1

    def __create_edit_button(self, frame, uuid: UUID, place: int, name: str):
        return gf.create_button_with_image(frame, self.__editIcon, partial(self.__paramsView.feed_params, uuid, name), place, 3)

    def __create_move_button(self, frame, uuid: UUID, text: str, row: int, column: int, up):
        return gf.create_button_with_image(frame, text, partial(self.move, uuid, up), row, column)

    def __create_delete_button(self, frame, uuid: UUID, place: int):
        return gf.create_button_with_image(frame, self.__deleteIcon, partial(self.remove, uuid), place, 4)

    def __get_id(self, uuid: UUID):
        return next(i for i, step in enumerate(
            self.__stepList) if step[0] == uuid)

    def move(self, uuid: UUID, up):
        id = self.__get_id(uuid)
        if (id is None):
            return

        new_id = (max(-1, id-1) if up else min(self.__get_last_item(), id+1))
        self.__stepList.insert(new_id, self.__stepList.pop(id))
        [step[id_widget].grid(row=i, column=id_widget) for id_widget in range(
            1, 6) for i, step in enumerate(self.__stepList)]
        self.__algorithmController.move_step(uuid, new_id)

        uuid = self.__stepList[id][0]

    def remove(self, uuid):
        id = self.__get_id(uuid)
        if (id is None):
            return

        [self.__stepList[id][id_widget].destroy() for id_widget in range(1, 6)]
        self.__stepList.remove(self.__stepList[id])

    def __play(self):
        self.__runnerController.play()
