from tensorflow.keras.models import load_model
import pandas as pd


class AI:
    def __init__(self):
        pass

    def load_model(self, filePath):
        self.__model = load_model(filePath)

    def load_labels(self, path: str, column: str):
        y_test = pd.read_csv(path)
        self.__labels = y_test[column].values

    def predict(self, img):
        return self.__model.predict(img)
