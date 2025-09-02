import json
import requests
import allure
from configuration.headers import Headers
from helpers.helper import Helper
from utilities.logger import logger


class RequestClient(Helper):
    """
    HTTP client wrapping requests.Session, with built-in logging, allure integration, and Pydantic validation
    """

    def __init__(self, base_url: str, token: str = None, extra_headers: dict = None):
        headers = Headers(token=token, extra_headers=extra_headers).get_headers()
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.session.headers.update(headers)

    def _log_request(self, method: str, url: str, **kwargs):
        logger.info(f"{method.upper()} {url}")
        if method.upper() != "GET" and "json" in kwargs:
            allure.attach(
                name="Request Payload",
                body=json.dumps(kwargs["json"], indent=2),
                attachment_type=allure.attachment_type.JSON
            )

    def _log_response(self, response: requests.Response):
        logger.info(f"Response {response.status_code} for {response.url}")
        try:
            payload = response.json()
            allure.attach(
                name="Response Body",
                body=json.dumps(payload, indent=2),
                attachment_type=allure.attachment_type.JSON
            )
        except ValueError:
            logger.warning("Non-JSON response body")

    def _request(self, method: str, path: str, **kwargs) -> requests.Response:
        url = path if path.startswith("https://") else f"{self.base_url}{path}"
        self._log_request(method, url, **kwargs)
        response = self.session.request(method=method, url=url, **kwargs)
        self._log_response(response)
        response.raise_for_status()
        return response

    def get_method(self, model=None, path: str = None, params: dict = None, return_json: bool = False):
        resp = self._request(method="get", path=path, params=params)
        return self._validate_response(resp, model, return_json=return_json)

    def get_method_for_files(self, path: str = None, params: dict = None, file_type: str = None):
        if file_type == "pdf":
            self.session.headers['Content-Type'] = 'application/pdf'
            resp = self._request(method="get", path=path, params=params)
        elif file_type == "doc":
            self.session.headers['Content-Type'] = 'application/msword'
            resp = self._request(method="get", path=path, params=params)
        elif file_type == "docx":
            self.session.headers['Content-Type'] = 'application/vnd.ms-word'
            resp = self._request(method="get", path=path, params=params)
        elif file_type == "xlsx":
            self.session.headers['Content-Type'] = 'application/vnd.ms-excel'
            resp = self._request(method="get", path=path, params=params)
        else:
            self.session.headers['Content-Type'] = 'application/vnd.ms-excel'
            resp = self._request(method="get", path=path, params=params)
        return self._validate_response(resp)

    def post_method(self,
                    model=None,
                    path: str = None,
                    json_data: dict = None,
                    files: dict = None,
                    return_json: bool = False,
                    expected_status: int = 200,
                    params: dict = None,
                    data: dict = None):
        if files:
            self.session.headers["Content-Type"] = "multipart/form-data"
            resp = self._request("post", path=path, files=files)
        elif data:
            self.session.headers["Content-Type"] = "application/x-www-form-urlencoded"
            resp = self._request("post", path=path, data=data)
        else:
            self.session.headers["Content-Type"] = "application/json"
            resp = self._request("post", path=path, json=json_data, params=params)
        return self._validate_response(resp, model, expected_status=expected_status, return_json=return_json)

    def put_method(self, model=None, path: str = None, json_data: dict = None, return_json: bool = False):
        resp = self._request("put", path=path, json=json_data)
        return self._validate_response(resp, model, return_json=return_json)

    def delete_method(self, model=None, path: str = None, return_json: bool = False):
        resp = self._request("delete", path=path)
        return self._validate_response(resp, model, return_json=return_json)

    def post_method_simple(self, model=None,
                           path: str = None,
                           return_json: bool = False,
                           expected_status: int = 200,
                           data: dict = None):
        resp = self._request("post", path=path, data=data)
        return self._validate_response(resp, model, expected_status=expected_status, return_json=return_json)

    def patch_method(self,
                     model=None,
                     path: str = None,
                     json_data: dict = None,
                     files: dict = None,
                     return_json: bool = False,
                     expected_status: int = 200,
                     params: dict = None,
                     data: dict = None):
        if files:
            self.session.headers["Content-Type"] = "multipart/form-data"
            resp = self._request("patch", path=path, files=files)
        elif data:
            self.session.headers["Content-Type"] = "application/x-www-form-urlencoded"
            resp = self._request("patch", path=path, data=data)
        else:
            self.session.headers["Content-Type"] = "application/json"
            resp = self._request("patch", path=path, json=json_data, params=params)

        return self._validate_response(resp, model, expected_status=expected_status, return_json=return_json)
