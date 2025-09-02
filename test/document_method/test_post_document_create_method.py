import pytest
from dotenv import set_key
from configuration.base_test import BaseTest
from servises.Document.document_payloads import document_create_payloads, document_access_payloads
from pathlib import Path


class TestPostDocumentMethod(BaseTest):

    @pytest.mark.post_document
    @pytest.mark.post_document_create
    def test_post_document(self):
        response = self.document_api.post_document.post_document_create_selector(json_data=document_create_payloads)
        assert response.status_code == 201
        guid = response.json()['data']['document']['guid']
        file_path =Path("guid_id")
        set_key(str(file_path),"GUID",guid)
        print(response.json())

    @pytest.mark.post_document
    @pytest.mark.post_document_access
    def test_post_document_access(self):
        response = self.document_api.post_document.post_document_access_selector(json_data=document_access_payloads)
        assert response.status_code == 200
        print(response.json())