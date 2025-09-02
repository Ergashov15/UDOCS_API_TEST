from typing import Optional, Dict, Any
from configuration.base_api import BaseAPI
from servises.Authentication.endpoint_authentication.endpoint_authentication import AuthenticationEndpoint
from servises.Authentication.model_authentication.model_authentication import ResponseAuthModel
from utilities.logger import logger


class PostAuthenticationSelector:
    def __init__(self, api: BaseAPI):
        self.client = api.client
        self.logger =logger
        self.endpoint =AuthenticationEndpoint


    def _post(self,path:str, model =None, json_data: Optional[Dict[str,Any]]=None, return_json:bool=True,
              expected_status: int =201):
        return self.client.post_method(
            model=model,
            path=path,
            json_data=json_data,
            expected_status=expected_status,
            return_json=return_json,
        )

    def authentication_post_selector(self,
                                     json_data: Optional[Dict[str,Any]] = None,
                                     return_json:bool=True,
                                     expected_status: int =200, username_=None, password_=None):
        path =self.endpoint.auth_login_end(username_,password_)
        return self._post(
            path=path,
            model =ResponseAuthModel,
            json_data=json_data,
            return_json=return_json,
            expected_status=expected_status,
        )
