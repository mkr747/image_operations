from PIL import ImageTk

from app.tools.gui_builder import GUIBuilder as gb


class ImageView:
    def __init__(self):
        pass

    def create(self, window, width=300, height=900):
        self.frame = gb.create_frame(window, width, height)
        self.__label_img.pack()
        self.__listbox.place()

    def set_image(self, img):
        self.__img = ImageTk.PhotoImage(image=img)
        self.__label_img = gb.create_image_label(self.frame, self.__img, 0, 0)

    def play(self):
        pass

    def stop(self):
        pass
