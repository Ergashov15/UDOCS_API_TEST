from typing import Optional
from configuration.base_api import BaseAPI
from servises.Document.endpoint_document.document_endpoint import DocumentEndpoint
from servises.Document.model_document.delete_document_guid_step_model import ResponseDeleteModel
from utilities.logger import logger


class DeleteMethodDocumentSelector:

    def __init__(self, base_api: BaseAPI):
        self.client = base_api.client
        self.logger = logger
        self.endpoint = DocumentEndpoint


    def _delete(self, path: str, model=None, param: str = None, return_json: bool = True):
        return self.client.get_method(
            model=model,
            path=path,
            params=param,
            return_json=return_json
        )


    def delete_document_guid_steps_selector(self,param: str = None, return_json: bool = True,document_guid_delete_id_step=None):
        model =ResponseDeleteModel
        url=self.endpoint.delete_guid_steps(document_guid_delete_id_step=document_guid_delete_id_step)
        return self._delete(path=url, model=model, param=param, return_json=return_json)
