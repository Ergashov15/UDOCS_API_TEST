class DocumentEndpoint:

    ENDPOINT = "/client/document"
    GET_STATUSES = f"{ENDPOINT}/statuses"
    DOCUMENT_CREATE = f"{ENDPOINT}/create"
    DOCUMENT_ACCESS = f"{ENDPOINT}/access"

    @staticmethod
    def get_documents(from_date, to_date):
        return "/client/documents?from_date={}&to_date={}".format(from_date, to_date)

    @staticmethod
    def document_example(template):
        return "/client/document/example?template={}".format(template)

    @staticmethod
    def get_documents_guid(guid_id_):
        return "/client/documents/{}".format(guid_id_)

    @staticmethod
    def get_document_guid_steps(document_guid_id_step):
        return "/client/documents/{}/steps".format(document_guid_id_step)

    @staticmethod
    def delete_guid_steps(document_guid_delete_id_step):
        return "/client/documents/{}/steps".format(document_guid_delete_id_step)

    @staticmethod
    def get_document_guid_client_pdf(guid_id_client_pdf):
        return f"/client/documents/{guid_id_client_pdf}/client-pdf"

    @staticmethod
    def get_client_pdf_qr_code(client_pdf_qr_code):
        return f"/client/documents/{client_pdf_qr_code}/client-pdf-with-qr-code"

    @staticmethod
    def get_guid_pdf(guid_pdf):
        return f"/client/documents/{guid_pdf}/pdf"

