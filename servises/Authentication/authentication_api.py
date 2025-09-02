from configuration.base_api import BaseAPI
from servises.Authentication.method_authentication.post_method_authentication import PostAuthenticationSelector


class AuthenticationAPI(BaseAPI):

    def __init__(self):
        super().__init__()
        self.post_authentication = PostAuthenticationSelector(self)