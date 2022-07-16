from enum import Enum


class CommandEnum(Enum):
    ERODE = "Erode",
    DILATE = "Dilate",
    OPENING = "Opening",
    CLOSING = "Closing",
    GRADIENT = "Gradient",
    SHAPE_DETECTION = "Shape detection",
    HU_MOMENTS_WITH_COUNTOURS = "Draw contours based on hu moments"
    MOMENTS_WITH_CONTOURS = "Draw contours based on moments"
    DRAW_CONTOURS = "Draw contours",
    THRESHOLDING = "Thresholding",
    CHANGE_COLOR_SPACE = "Transfrom color space",
    AI_WITH_CONTOURS = "AI"
