from typing import Optional, Dict, Any
from configuration.base_api import BaseAPI
from servises.Templates.endpoint_templates.endpoint_templates import TemplatesEndpoint
from servises.Templates.model_templates.document_templates_model import ResponseTemplateModel
from utilities.logger import logger


class PostDocumentExemplarSelector:
    def __init__(self, api: BaseAPI):
        self.client = api.client
        self.logger =logger
        self.endpoint = TemplatesEndpoint


    def _post(self,path:str, model =None, json_data: Optional[Dict[str,Any]]=None, return_json:bool=True,
              expected_status: int =201):
        return self.client.post_method(
            model=model,
            path=path,
            json_data=json_data,
            expected_status=expected_status,
            return_json=return_json,
        )

    def document_exemplar_selector(self,
                                   json_data: Optional[Dict[str, Any]] = None,
                                   return_json: bool = True,
                                   expected_status: int = 200,template=None):

        path =self.endpoint.document_exemplar(template=template)
        return self._post(
            path=path,
            model=ResponseTemplateModel,
            json_data=json_data,
            return_json=return_json,
            expected_status=expected_status
        )

