class Resolution:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, val):
        self.__width = val

    @height.setter
    def height(self, val):
        self.__height = val

    @width.deleter
    def width(self):
        del self.__width

    @height.deleter
    def height(self):
        del self.__height
