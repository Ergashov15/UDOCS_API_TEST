from ctypes import c_char

import pytest
from configuration.base_test import BaseTest
from servises.Client.client_payloads import client_payloads

class TestClientUpdate(BaseTest):

    @pytest.mark.client
    @pytest.mark.client_update
    def test_client_update(self):
        response = self.client_api.post_client.config_update_selector(json_data=client_payloads)
        assert response.status_code == 200
        print(response.json())