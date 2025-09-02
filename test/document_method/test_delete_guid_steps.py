import pytest
from configuration.base_test import BaseTest
from utilities.validation_for_json import assertion_json_from_dict

class TestDeleteGuidSteps(BaseTest):
    #CONSTANTA
    GUID= '0736bc2d-7229-4376-a543-ff780d9c486c'

    @pytest.mark.delete_guid
    @pytest.mark.delete_guid_step
    def test_delete_guid(self):
        response =self.document_api.delete_document.delete_document_guid_steps_selector(document_guid_delete_id_step=self.GUID)
        assert response.status_code == 200