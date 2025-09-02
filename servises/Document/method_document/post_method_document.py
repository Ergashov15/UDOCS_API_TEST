from typing import Optional, Dict, Any
from configuration.base_api import BaseAPI
from servises.Document.endpoint_document.document_endpoint import DocumentEndpoint
from servises.Document.model_document.post_document_access_model import ResponseDocumentAccessModel
from servises.Document.model_document.post_document_create_model import ResponseDocumentCreateModel
from utilities.logger import logger


class PostDocumentSelector:
    def __init__(self, api: BaseAPI):
        self.client = api.client
        self.logger =logger
        self.endpoint =DocumentEndpoint

    def _post(self,path:str, model =None, json_data: Optional[Dict[str,Any]]=None, return_json:bool=True,
              expected_status: int =201):
        return self.client.post_method(
            model=model,
            path=path,
            json_data=json_data,
            expected_status=expected_status,
            return_json=return_json,
        )
    def post_document_create_selector(self,
                             json_data: Optional[Dict[str,Any]] = None,
                             expected_status: int =201,
                             return_json:bool=True,):
        path =self.endpoint.DOCUMENT_CREATE
        return self._post(
            path=path,
            model=ResponseDocumentCreateModel,
            json_data=json_data,
            expected_status=expected_status,
            return_json=return_json,
        )

    def post_document_access_selector(self,
                             json_data: Optional[Dict[str,Any]] = None,
                             expected_status: int =200,
                             return_json:bool=True,):
        path =self.endpoint.DOCUMENT_ACCESS
        return self._post(
            path=path,
            model=ResponseDocumentAccessModel,
            json_data=json_data,
            expected_status=expected_status,
            return_json=return_json,
        )