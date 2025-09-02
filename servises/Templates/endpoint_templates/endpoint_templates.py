class TemplatesEndpoint:

    ENDPOINT = "/client"
    #DOCUMENT_EXAMPLE_URL = f"{ENDPOINT}/document/exemplar/"
    @staticmethod
    def document_exemplar(template):
        return "/client/document/exemplar?template={}".format(template)

