from configuration.base_api import BaseAPI
from servises.Templates.method_templates.post_document_exemplar_method import PostDocumentExemplarSelector


class TemplatesAPI(BaseAPI):
    def __init__(self, ):
        super().__init__()
        self.post_template_exemplar = PostDocumentExemplarSelector(self)