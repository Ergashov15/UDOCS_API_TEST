import time
import pytest
from configuration.base_test import BaseTest
from utilities.validation_for_json import assertion_json_from_dict
from utilities.pdf_file_saver import save_response_to_file, assertion_for_bytes
from dotenv import get_key
from pathlib import Path

class TestGetDocumentMethod(BaseTest):
    # CONSTANTA
    TEMPLATE = "cyber_sec_test"
    FROM_DATE = '2025-07-11'
    TO_DATE = '2025-07-11'
    GUID = '0736bc2d-7229-4376-a543-ff780d9c486c'
    IMPORTANT_FIELDS = ['number']
    IMPORTANT_FIELDS_FOR_GET = ['current_page', 'data']
    IMPORTANT_FIELDS_FOR_GUID = ['guid']

    # @pytest.mark.document
    # @pytest.mark.get_document_example
    # def test_get_document_example(self):
    #     response = self.document_api.get_document.get_document_example_selector(template=self.TEMPLATE)
    #     assert response.status_code == 201
    #     assertion_json_from_dict(response=response.json()['data'],
    #                              important_fields=self.IMPORTANT_FIELDS_FOR_GET,
    #                              from_where_to_find_in_list="data")
    #///////////////////////////////////////////////////////////////////////////////////////

    @pytest.mark.get_document
    @pytest.mark.get_documents_method_doc
    def test_get_documents(self):
        response = self.document_api.get_document.get_client_documents_selector(from_date=self.FROM_DATE,
                                                                                to_date=self.TO_DATE)
        assert response.status_code == 200
        assertion_json_from_dict(response=response.json()['data'],
                                 important_fields=self.IMPORTANT_FIELDS_FOR_GET,
                                 from_where_to_find_in_list='documents')

    # ///////////////////////////////////////////////////////////////////////////////////////

    @pytest.mark.get_document
    @pytest.mark.get_documents_guid
    def test_get_documents_guid(self):
        file_path = Path("guid_id")
        guid = get_key(str(file_path), "GUID")
        response = self.document_api.get_document.get_client_documents_guid_selector(guid_id=guid)
        assert response.status_code == 200
        assertion_json_from_dict(response=response.json()['data'],
                                 important_fields=self.IMPORTANT_FIELDS_FOR_GUID,
                                 from_where_to_find_in_list='data/owner')

    # ///////////////////////////////////////////////////////////////////////////////////////

    @pytest.mark.get_document
    @pytest.mark.get_documents_guid_step
    def test_get_documents_guid_step(self):
        file_path = Path("guid_id")
        guid = get_key(str(file_path), "GUID")
        response = self.document_api.get_document.get_client_documents_guid_steps_selector(
            document_guid_id_step=guid)
        assert response.status_code == 200
        assertion_json_from_dict(response=response.json()['data'],
                                 important_fields=self.IMPORTANT_FIELDS_FOR_GUID,
                                 from_where_to_find_in_list='document')

    # ///////////////////////////////////////////////////////////////////////////////////////

    @pytest.mark.get_document
    @pytest.mark.get_documents_status
    def test_get_documents_status(self):
        response = self.document_api.get_document.get_statuses_selector()
        assert response.status_code == 200

    # ///////////////////////////////////////////////////////////////////////////////////////

    @pytest.mark.get_document
    @pytest.mark.get_documents_guid_pdf
    def test_get_documents_pdf(self):
        file_path = Path("guid_id")
        guid = get_key(str(file_path), "GUID")
        response = self.document_api.get_document.get_client_documents_guid_pdf_selector(guid_pdf=guid)
        file_path = f"files/inner_files/get_documents_guid_pdf.pdf"
        save_response_to_file(file_path=file_path, response_data=response)

    # ///////////////////////////////////////////////////////////////////////////////////////

    @pytest.mark.get_document
    @pytest.mark.get_documents_guid_client_pdf
    def test_documents_client_pdf(self):
        file_path = Path("guid_id")
        guid = get_key(str(file_path), "GUID")
        response = self.document_api.get_document.get_client_documents_guid_client_pdf_selector(
            guid_id_client_pdf=guid)
        file_path = f"files/inner_files/documents_client_pdf.pdf"
        save_response_to_file(file_path=file_path, response_data=response)

    # ///////////////////////////////////////////////////////////////////////////////////////

    @pytest.mark.get_document
    @pytest.mark.get_documents_guid_client_pdf_qr_code
    def test_documents_guid_client_qr_code(self):
        file_path = Path("guid_id")
        guid = get_key(str(file_path), "GUID")
        response = self.document_api.get_document.get_client_documents_guid_pdf_qr_code_selector(
            client_pdf_qr_code=guid)
        file_path = f"files/inner_files/documents_client_pdf_qr_code.pdf"
        save_response_to_file(file_path=file_path, response_data=response)



