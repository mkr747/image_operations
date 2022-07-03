import tkinter as tk
from uuid import UUID

from app.controllers.params_controller import ParamsController
from app.services.commands.command import Command
from app.factories.gui_factory import GUIBuilder as gb


class AlgorithmView:
    def __init__(self, paramsController: ParamsController):
        self.__paramsController = paramsController
        self.__order = []
        self.__editButtons = []

    def create(self, window, width=300, height=900):
        self.frame = gb.create_frame(window, width, height)
        self.__listbox = gb.create_listbox(self.frame)
        self.__listbox.place()

    def append(self, step: Command):
        checkbutton = gb.create_checkbox(self.__listbox, step.get_name())
        self.__listbox.insert(tk.END, checkbutton)
        self.__order.append(step.uuid)

        self.__editButtons.append(self.__create_edit_button(
            step.uuid, len(self.__editButtons)))

    def move(self, step: Command, place: int):
        id = self.__order.index(step.uuid)
        if (~id):
            return

        checkbutton = gb.create_checkbox(self.__listbox, step.get_name())
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
        return gb.create_button(self.frame, 'Edit', self.__paramsController.feed_params(uuid), place, 1)
