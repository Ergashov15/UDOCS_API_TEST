from typing import Optional, Dict, Any
from configuration.base_api import BaseAPI
from servises.Client.endpoint_client.endpoint_client import ClientEndpoint
from servises.Client.model_client.client_model import ResponseConfigUpdateModel
from utilities.logger import logger


class PostClientSelector:
        def __init__(self, api: BaseAPI):
            self.client = api.client
            self.logger = logger
            self.endpoint = ClientEndpoint

        def _post(self, path: str, model=None, json_data: Optional[Dict[str, Any]] = None, return_json: bool = True,
                  expected_status: int = 201):
            return self.client.post_method(
                model=model,
                path=path,
                json_data=json_data,
                expected_status=expected_status,
                return_json=return_json,
            )
        def config_update_selector(self,
                                   json_data: Optional[Dict[str, Any]] = None,
                                   expected_status: int = 200,
                                   return_json: bool = True,):
            path =self.endpoint.CONFIG_UPDATE
            return self._post(
                path=path,
                model=ResponseConfigUpdateModel,
                json_data=json_data,
                expected_status=expected_status,
                return_json=return_json,
            )