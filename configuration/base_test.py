from servises.Authentication.authentication_api import AuthenticationAPI
from servises.Templates.templates_api import TemplatesAPI
from servises.Document.document_api import DocumentApi
from servises.Client.client_api import ClientAPI
class BaseTest:

    def setup_method(self):
        self.authentication_api = AuthenticationAPI()
        self.template_api = TemplatesAPI()
        self.document_api = DocumentApi()
        self.client_api = ClientAPI()
        
