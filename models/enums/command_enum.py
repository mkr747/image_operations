from enum import Enum


class CommandEnum(Enum):
    ERODE = "Erode",
    DILATE = "Dilate",
    OPENING = "Opening",
    CLOSING = "Closing",
    GRADIENT = "Gradient",
    SHAPE_DETECTION = "Shape detection",
    DRAW_CONTOURS = "Draw contours",
    THRESHOLDING = "Thresholding",
    CHANGE_COLOR_SPACE = "Transfrom color space",
    AI = "AI"
