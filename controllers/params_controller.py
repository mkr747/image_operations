from typing import Dict, List
from uuid import UUID
from models.parameter_widget import ParameterWidget
from models.params_metadata import ParamsMetadata
from services.params_service import ParamsService


class ParamsController:
    def __init__(self, paramsService: ParamsService):
        self.__paramsService = paramsService

    def set_params(self, uuid: UUID, params: Dict[str, ParamsMetadata]):
        self.__paramsService.set_params(uuid, params)

    def get_params(self, uuid: UUID) -> List[ParameterWidget]:
        return self.__paramsService.get_params(uuid)
