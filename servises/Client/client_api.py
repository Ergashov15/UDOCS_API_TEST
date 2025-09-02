from configuration.base_api import BaseAPI
from servises.Client.method_client.post_method_client import PostClientSelector


class ClientAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.post_client = PostClientSelector(self)
