from typing import Optional
import requests
from configuration.base_api import BaseAPI
from servises.Document.endpoint_document.document_endpoint import DocumentEndpoint
from servises.Document.model_document.document_example_model import ResponseDocumentExampleModel
from servises.Document.model_document.documents_guid_steps_model import ResponseGuidStepsModel
from servises.Document.model_document.get_document_guid_model import ResponseDocumentGuidModel
from servises.Document.model_document.get_documents_model import  ResponseGetDocumentsModel
from servises.Document.model_document.get_status_model import ResponseStatusModel
from utilities.logger import logger

class GetDocumentSelector:

    def __init__(self, base_api: BaseAPI):
        self.client = base_api.client
        self.logger = logger
        self.endpoint = DocumentEndpoint


    def _get(self, path: str, model=None, param: str = None, return_json: bool = True):
        return self.client.get_method(
            model=model,
            path=path,
            params=param,
            return_json=return_json
        )

    def get_document_example_selector(self,param: Optional[str] = None, return_json: bool = True, template=None):
        model = ResponseDocumentExampleModel,
        url = self.endpoint.document_example(template=template)
        return self._get(path=url, model=model, return_json=return_json,param=param)

    def get_client_documents_selector(self, param: Optional[str] = None, return_json: bool = True, from_date=None, to_date=None):
        model = ResponseGetDocumentsModel
        url= self.endpoint.get_documents(from_date=from_date, to_date=to_date)
        return self._get(path=url, model=model, return_json=return_json,param=param)

    def get_client_documents_guid_selector(self, param: Optional[str] = None, return_json: bool = True,guid_id=None):
         model = ResponseDocumentGuidModel
         url=self.endpoint.get_documents_guid(guid_id_=guid_id)
         return self._get(path=url, model=model, return_json=return_json,param=param)

    def get_client_documents_guid_steps_selector(self, param: Optional[str] = None, return_json: bool = True,document_guid_id_step=None):
        model = ResponseGuidStepsModel
        url=self.endpoint.get_document_guid_steps(document_guid_id_step=document_guid_id_step)
        return self._get(path=url, model=model, return_json=return_json,param=param)

    def get_client_documents_guid_client_pdf_selector(self, guid_id_client_pdf: str):
        url = self.endpoint.get_document_guid_client_pdf(guid_id_client_pdf)
        return self.client.get_method_for_files(path=url)

    def get_client_documents_guid_pdf_qr_code_selector(self, client_pdf_qr_code: str):
        url = self.endpoint.get_client_pdf_qr_code(client_pdf_qr_code)
        return self.client.get_method_for_files(path=url)

    def get_client_documents_guid_pdf_selector(self, guid_pdf: str):
        url = self.endpoint.get_guid_pdf(guid_pdf)
        return self.client.get_method_for_files(path=url)

    def get_statuses_selector(self, param: Optional[str] = None, return_json: bool = True):
        model = ResponseStatusModel
        url=self.endpoint.GET_STATUSES
        return self._get(path=url, model=model, return_json=return_json,param=param)

