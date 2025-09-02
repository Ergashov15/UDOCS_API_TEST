import pytest
from configuration.base_test import BaseTest

class TestTemplateExemplar(BaseTest):
    #CONSTANTA

    @pytest.mark.template
    @pytest.mark.template_exemplar
    def test_template_exemplar(self):
        response =self.template_api.post_template_exemplar.document_exemplar_selector(template='cyber_sec_test')
        assert response.status_code == 200
        print(response.json())