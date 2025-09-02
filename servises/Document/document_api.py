from configuration.base_api import BaseAPI
from servises.Document.method_document.get_method_document import GetDocumentSelector
from servises.Document.method_document.post_method_document import PostDocumentSelector
from servises.Document.method_document.delete_method_document import DeleteMethodDocumentSelector

class DocumentApi(BaseAPI):
    def __init__(self):
        super().__init__()
        self.post_document = PostDocumentSelector(self)
        self.get_document = GetDocumentSelector(self)
        self.delete_document = DeleteMethodDocumentSelector(self)