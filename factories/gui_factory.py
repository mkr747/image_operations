import tkinter as tk
import tkinter.ttk as ttk


class GuiFactory:
    @staticmethod
    def create_frame(frame, width, height) -> ttk.Frame:
        return ttk.Frame(master=frame, width=width, height=height)

    @staticmethod
    def create_label(frame: ttk.Frame, text: str, row: int, column: int) -> ttk.Label:
        label = ttk.Label(frame, text=text)
        label.grid(row=row, column=column)

        return label

    @staticmethod
    def create_combobox(frame: ttk.Frame, values: list, is_readonly: bool, row: int, column: int) -> ttk.Combobox:
        print('tak')
        state = 'readonly' if is_readonly else 'normal'
        combobox = ttk.Combobox(master=frame, values=values, state=state)
        combobox.grid(row=row, column=column)

        return combobox

    @staticmethod
    def create_image_label(frame: ttk.Frame, img: any, row: int, column: int) -> ttk.Label:
        label = tk.Label(frame, image=img)
        label.grid(row=row, column=column)

        return label

    @staticmethod
    def create_entry(frame: ttk.Frame, row: int, column: int) -> ttk.Entry:
        entry = ttk.Entry(frame)
        entry.grid(row=row, column=column)

        return entry

    @staticmethod
    def create_button(frame: ttk.Frame, text: str, command: any, row: int, column) -> ttk.Button:
        button = ttk.Button(frame, text=text, command=command)
        button.grid(column=column, row=row)

        return button

    @staticmethod
    def create_button_with_image(frame: ttk.Frame, image: tk.PhotoImage, command: any, row: int, column) -> ttk.Button:
        button = ttk.Button(frame, image=image, command=command)
        button.grid(column=column, row=row)

        return button

    @staticmethod
    def create_checkbox(frame: any, text: str, enabled: bool, row: int, column: int, sticky: str) -> ttk.Checkbutton:
        checkbutton = ttk.Checkbutton(
            frame, text=text, command=(lambda: print(enabled.get())), variable=enabled, onvalue=True, offvalue=False)
        checkbutton.grid(row=row, column=column, sticky=sticky)

        return checkbutton

    @staticmethod
    def create_listbox(frame: any, row: int, column: int) -> tk.Listbox:
        listbox = tk.Listbox(frame)
        listbox.grid(row=row, column=column)

        return listbox

    @staticmethod
    def create_scale(frame: ttk.Frame, limit: int, row: int, column: int) -> ttk.Scale:
        scale = ttk.Scale(frame, from_=0, to=limit, orient=tk.HORIZONTAL)
        scale.grid(row=row, column=column)

        return scale
