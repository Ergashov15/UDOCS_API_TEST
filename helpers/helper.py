import json
from pydantic import  BaseModel, ValidationError
import allure
import requests

class Helper:
    def attach_response(self, response_json):
        try:
            attachment = json.dumps(response_json, indent=4)
            allure.attach(
                name="API Response",
                body=attachment,
                attachment_type=allure.attachment_type.JSON,
            )
        except Exception as e:
            print(f"Error attaching response: {e}")

    def _validate_response(self, response: requests.Response,model:type[BaseModel]= None,expected_status: int=200,
                           return_json: bool=False):
        try:
            json_data = response.json()
        except ValueError:
            if not model:
                return response if return_json else response.content
            else:
                raise ValueError("Response is not JSON , but validation was requested.")
        self.attach_response(json_data)

        if response.status_code != expected_status:
            raise AssertionError(f"Expected {expected_status},got {response.status_code}")

        if model:
            try:
                if isinstance(json_data, dict):
                    validated = model(**json_data)
                elif isinstance(model, tuple):
                    model = model[0]
                elif isinstance(json_data, list):
                    validated =[model(**item) for item in json_data]
                response.parsed = validated
            except ValidationError as e:
                print(f"Validation error: {e}")
                raise
        return  response

