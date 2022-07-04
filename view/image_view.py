from tkinter.messagebox import showinfo
from PIL import ImageTk
from tkinter import filedialog as fd
from controllers.image_controller import ImageController

from factories.gui_factory import GuiFactory as gb


class ImageView:
    def __init__(self, imageController: ImageController):
        self.__imageController = imageController

    def create(self, window, width=300, height=900):
        self.__frame = gb.create_frame(window, width, height)
        self.__import_file_button = gb.create_button(
            window, 'Load image/video', self.__load_data())
        self.__play_button = gb.create_button(
            window, 'Play', self.__play())

        self.__stop_button = gb.create_button(window, 'Stop', self.__stop())
        self.__label_img = gb.create_image_label(
            self.__frame, self.__img, 0, 0)

        return self.__frame

    def __set_image(self, img):
        self.__img = ImageTk.PhotoImage(image=img)
        self.__label_img.configure(image=self.__img)
        self.__label_img.image = self.__img

    def __play(self):
        while self.__imageController.is_playing():
            self.__set_image(self.__imageController.get_current_image())

    def __stop(self):
        self.__imageController.stop()

    def __load_data(self):
        filetypes = (
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

        showinfo(
            title='Selected Files',
            message=filenames
        )
