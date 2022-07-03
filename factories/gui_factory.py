import tkinter as tk
import tkinter.ttk as ttk


class GuiFactory:
    @staticmethod
    def create_frame(frame, width, height):
        return ttk.Frame(master=frame, width=width, height=height)

    @staticmethod
    def create_label(frame: ttk.Frame, text: str, row: int, column: int):
        return ttk.Label(frame, text=text).grid(row=row, column=column)

    @staticmethod
    def create_image_label(frame: ttk.Frame, img: any, row: int, column: int):
        return ttk.Label(frame, image=img).grid(row=row, column=column)

    @staticmethod
    def create_entry(frame: ttk.Frame, row: int, column: int):
        return ttk.Entry(frame).grid(row=row, column=column)

    @staticmethod
    def create_button(frame: ttk.Frame, text: str, command: any, row: int, column):
        return ttk.Button(frame, text=text).grid(column=column, row=row, command=command)

    @staticmethod
    def create_checkbox(frame: any, text: str):
        return ttk.Checkbutton(frame, text=text)

    @staticmethod
    def create_listbox(frame: any):
        return tk.Listbox(frame)
