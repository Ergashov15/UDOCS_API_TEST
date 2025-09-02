from client.api_client import RequestClient
from configuration.tokens_and_url import TOKENS,BASE_URL

class BaseAPI:

    def __init__(self,token_key: str ="default", base_url: str ="default"):

        base_url = BASE_URL.get(base_url)
        if not base_url:
            raise ValueError("BASE_URL is not set in env file")

        token = TOKENS.get(token_key)
        if not token:
            raise EnvironmentError(f"Token not found for key: {token_key}")

        self.client = RequestClient(base_url= base_url, token=token)


