from builders.params_builder import ParamsBuilder


class BuilderFactory:
    def __init__(self):
        pass

    def get_widget_builder(self):
        return ParamsBuilder()
