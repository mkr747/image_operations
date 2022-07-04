import tkinter as tk
from uuid import UUID

from controllers.params_controller import ParamsController
from controllers.runner_controller import RunnerController
from services.commands.command import Command
from factories.gui_factory import GuiFactory as gf


class AlgorithmView:
    def __init__(self, paramsController: ParamsController, runnerController: RunnerController):
        self.__paramsController = paramsController
        self.__runnerController = runnerController
        self.__order = []
        self.__editButtons = []

    def create(self, window, width=300, height=900):
        self.__frame = gf.create_frame(window, width, height)
        self.__listbox = gf.create_listbox(self.__frame)
        self.__playButton = gf.create_button(
            window, 'Play', self.__play(), 0, 0)
        self.__listbox.place()

        return self.__frame

    def append(self, step: Command):
        checkbutton = gf.create_checkbox(self.__listbox, step.get_name())
        self.__listbox.insert(tk.END, checkbutton)
        self.__order.append(step.uuid)

        self.__editButtons.append(self.__create_edit_button(
            step.uuid, len(self.__editButtons)))

    def move(self, step: Command, place: int):
        id = self.__order.index(step.uuid)
        if (~id):
            return

        checkbutton = gf.create_checkbox(self.__listbox, step.get_name())
        self.__editButtons[id].pack_forget()
        self.__listbox.delete(id)
        self.__editButtons.insert(place, self.__buttons.append(self.__create_edit_button(
            step.uuid, place)))
        self.__listbox.insert(place, checkbutton)

    def remove(self, uuid):
        id = self.__order.index(uuid)
        if (~id):
            return

        self.__listbox.delete(id)

    def param_details(self, uuid: UUID):
        self.__paramsController.set_params(uuid)

    def __create_edit_button(self, uuid: UUID, place: int):
        return gf.create_button(self.__frame, 'Edit', self.__paramsController.feed_params(uuid), place, 1)

    def __play(self):
        self.__runnerController.play()
