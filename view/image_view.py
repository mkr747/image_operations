from functools import partial
import threading
from tkinter.messagebox import showinfo
from PIL import ImageTk
from tkinter import filedialog as fd
import PIL

import numpy as np
from tools.utils import Utils
from controllers.image_controller import ImageController

from factories.gui_factory import GuiFactory as gb


class ImageView:
    def __init__(self, imageController: ImageController):
        self.__imageController = imageController
        self.__img = ImageTk.PhotoImage(PIL.Image.fromarray(
            np.zeros([100, 100, 3], dtype=np.uint8)))

    def create(self, window, width=300, height=900):
        self.__frame = gb.create_frame(window, width, height)
        self.__import_file_button = gb.create_button(
            self.__frame, 'Load image/video', threading.Thread(target=self.__load_data).start, 0, 0)
        self.__play_button = gb.create_button(
            self.__frame, 'Play', self.__play, 0, 1)
        self.__stop_button = gb.create_button(
            self.__frame, 'Stop', self.__stop, 0, 2)
        img = Utils.read_iamge('1.jpg')
        self.__img = img
        self.__label_img = gb.create_image_label(
            self.__frame, img, 1, 1)

        return self.__frame

    def __set_image(self, img):
        im = Utils.wrap_image(img)
        self.__img = im
        self.__label_img.configure(image=self.__img)
        self.__label_img.image = self.__img
        self.__label_img.update()

    def __play(self):
        print('clicked play')
        self.__imageController.play()
        while self.__imageController.is_playing():
            self.__set_image(self.__imageController.get_current_image())

    def __stop(self):
        self.__imageController.stop()

    def __load_data(self):
        filetypes = (
            ('all', '*'),
            ('movies', '*.mp4'),
            ('image jpg', '*.jpg'),
            ('image png', '*.png'),
            ('image jpeg', '*.jpeg')
        )

        filenames = fd.askopenfilenames(
            title='Open files',
            initialdir='/',
            filetypes=filetypes
        )

        self.__imageController.load(filenames)
