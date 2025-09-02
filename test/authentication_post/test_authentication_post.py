import pytest
from dotenv import set_key
from pathlib import Path
from configuration.base_test import BaseTest
from servises.Authentication.authentication_payloads import authentication_payloads


class TestAuthenticationPost(BaseTest):

    @pytest.mark.authentication
    @pytest.mark.authentication_post
    def test_authentication_post(self):
        response = self.authentication_api.post_authentication.authentication_post_selector(json_data=authentication_payloads)
        assert response.status_code == 200
        token = response.json()['data']['token']['access_token']
        env_path = Path(".env")
        set_key(str(env_path), "TOKEN", token)
        print(f"Successfully authorized: {token}")





