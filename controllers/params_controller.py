from services.algorithm_service import AlgorithmService
from view.params_view import ParamsView


class ParamsController:
    def __init__(self, algorithmService: AlgorithmService, paramsView: ParamsView):
        self.__algorithmService = algorithmService
        self.__paramsView = paramsView

    def set_params(self, uuid, params: dict):
        self.__algorithmService.set_params(uuid, params)

    def feed_params(self, uuid) -> None:
        self.__paramsView.set_params(self.__algorithmService.get_params(uuid))
