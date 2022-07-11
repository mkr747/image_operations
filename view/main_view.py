from tkinter import ttk
import tkinter
from factories.gui_factory import GuiFactory as gf
from view.algorithm_view import AlgorithmView

from view.components_view import ComponentView
from view.image_view import ImageView
from view.params_view import ParamsView


class MainView:
    def __init__(self, algorithmView: AlgorithmView, componentView: ComponentView, imageView: ImageView, paramsView: ParamsView):
        self.__algorithmView = algorithmView
        self.__componentView = componentView
        self.__imageView = imageView
        self.__paramsView = paramsView

    def create_main_view(self, window):
        window.rowconfigure(0, minsize=100, weight=1)
        window.columnconfigure(0, minsize=100, weight=1)

        s = ttk.Style()
        s.configure("TFrame", relief=tkinter.RAISED)

        frame_right = gf.create_frame(frame=window, width=1200, height=900)
        frame_components = self.__componentView.create(
            window=window, width=300, height=900)

        frame_algorithm = self.__algorithmView.create(
            window=frame_right, width=400, height=600)

        frame_image = self.__imageView.create(
            window=frame_right, width=800, height=600)

        frame_params = self.__paramsView.create(
            window=frame_right, width=400, height=300)

        frame_ai = gf.create_frame(frame=frame_right, width=800, height=300)

        frame_components.grid(row=0, column=0, padx=1, pady=1, sticky="nsew")
        frame_right.grid(row=0, column=1, padx=1, pady=1, sticky="nsew")
        frame_algorithm.grid(row=0, column=3, padx=1, pady=1, sticky="nsew")
        frame_image.grid(row=0, column=7, padx=1, pady=1, sticky="nsew")
        frame_params.grid(row=6, column=3, padx=1, pady=1, sticky="nsew")
        frame_ai.grid(row=6, column=7, padx=1, pady=1, sticky="nsew")
