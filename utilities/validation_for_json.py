from typing import List, Dict, Any

from _pytest.main import Failed


def assertion_json_from_dict_2(important_fields: list, response: dict, from_where_to_find_in_list="results"):
    """
        {
          "count": 5,
          "num_pages": 1,
          "current_page": 1,
          "page_size": 10,
          "next": null,
          "previous": null,
          "results": [
                {
                  "transaction_month": "2025-04-01T00:00:00",
                  "correction_volume": -1,
                  "correction_amount": -1,
                  "price": 25,
                  "filling_station_id": 19,
                  "volume": 153762.005,
                  "amount": 3844050.125,
                  "balance": 9557630439368.03,
                  "invoice_number": null
                },
                {
                  "transaction_month": "2025-03-01T00:00:00",
                  "correction_volume": 546,
                  "correction_amount": 13650,
                  "price": 25,
                  "filling_station_id": 19,
                  "volume": 216878.68,
                  "amount": 5421967,
                  "balance": 86775102.945,
                  "invoice_number": "100"
                }
            ]
            }

            will check inside of results list
    """
    try:
        for index, result in enumerate(response[from_where_to_find_in_list]):
            for field in important_fields:
                assert field in result, f"Field '{field}' missing in item: "
                assert result[field] is not None, f"Field '{field}' is None in item: "
    except KeyError as e:
        print(f"Missing field in result validation_json_from_dict : {e}")


def assertion_json_from_dict(important_fields: list, response: dict, from_where_to_find_in_list="results"):
    try:
        data = response.get(from_where_to_find_in_list, response)
        # Agar bu list bo‘lsa — iteratsiya qilamiz
        if isinstance(data, list):
            for index, result in enumerate(data):
                for field in important_fields:
                    assert field in result, f"Field '{field}' missing in item: {result}"
                    assert result[field] is not None, f"Field '{field}' is None in item: {result}"
                    if result[field] == 0:
                        assert False, f"Field '{field}' is 0 in item: {result}"
        # Aks holda, bitta dict bo‘lsa — bevosita tekshiramiz
        elif isinstance(data, dict):
            for field in important_fields:
                assert field in data, f"Field '{field}' missing in item: {data}"
                assert data[field] is not None, f"Field '{field}' is None in item: {data}"
        else:
            raise AssertionError("Unexpected data type in response.")
    except KeyError as e:
        print(f"Missing field in result validation_json_from_dict : {e}")


def assertion_json_from_list(important_fields: list, response):
    try:
        extracted_data = [{field: result[field] for field in important_fields} for result in response]
        for data in extracted_data:
            for field, value in data.items():
                assert value is not None, f"Field '{field}' is None in result: {data}"
    except KeyError as e:
        print(f"Missing field in result: {e}")


def assertion_json_from_json(important_fields: list, response):
    """
        {
            "id": 0,
            "password": "********",
            "email": "string",
        }
    """
    try:
        extracted_data = {field: response[field] for field in important_fields}  # NOT a list of dicts
        for field, value in extracted_data.items():
            assert value is not None, f"Field '{field}' is None in response: {response}"
    except KeyError as e:
        print(f"Missing field in response: {e}")


def check_important_fields_for_none(response: dict, important_fields: list) -> None:
    """
        {
          "price": "0.00",
          "cloud_price": "4100.00",
          "start_date": "23-04-2025"
        }
    """
    """Checks if all important fields exist and are not None in the response dictionary"""
    missing_or_none_fields = []

    for field in important_fields:
        if field not in response or response[field] is None:
            missing_or_none_fields.append(field)

    assert not missing_or_none_fields, (
        f"The following important fields are missing or None: {missing_or_none_fields}"
    )


def assert_required_fields_exist_and_not_null(response: List[Dict[str, Any]], important_fields: List[str]) -> None:
    """Assert that each dict in the list contains the required fields and that those fields are not None"""
    for i, item in enumerate(response):
        for field in important_fields:
            assert field in item, f"Missing field '{field}' in item {i}: {item}"
            assert item[field] is not None, f"Field '{field}' is None in item {i}: {item}"


def validate_list_dic_not_none(response: list, important_fields: list):
    """ EXAMPLE
        [
          {
            "region_code": "ALL",
            "region_name": "Barcha viloyatlar",
            "total_filling_station": 0
          }
        ]
    """
    for index, item in enumerate(response):
        for field in important_fields:
            assert item.get(field) is not None, f"'{field}' is None at index {index}"
            if item.get(field) == 0:
                assert False, f"'{field}' is 0 at index {index}"


def check_important_fields(response: Dict[str, Any], important_fields: List[str]) -> None:
    results = response.get("results", [])
    for i, item in enumerate(results):
        for field in important_fields:
            value = item.get(field, None)
            assert value is not None, f"Missing or null field '{field}' in result index {i}: {item}"


from typing import Dict, Any, List


def assert_required_fields(response: Dict[str, Any], important_fields: List[str]) -> None:
    """Assert that important fields exist and are not null in nested equipment structures."""
    field_map = {
        'cylinder_volume': response.get('accumulator', {}),
        'cylinder_count': response.get('accumulator', {}),
        'total_cylinder_volume': response.get('accumulator', {}),
        'avg_pressure': response.get('accumulator', {}),
        'avg_gas_volume': response.get('accumulator', {}),
        'percent': response.get('construction_regulation', {}),
    }

    for field in important_fields:
        container = field_map.get(field)
        assert container is not None, f"Container for field '{field}' is missing"
        assert field in container, f"Field '{field}' is missing in its container: {container}"
        assert container[field] is not None, f"Field '{field}' is None in its container: {container}"

    ####################################################################################################################
    ####################################################################################################################


def assert_validator(response, important_fields):
    """
        {
          "stations": [
            {
              "region_code": "10",
              "region_name": "TASHKENT CITY  ",
              "digitalized_count": 18,
              "un_digitalized_count": 35,
              "stations_count": [
                {
                  "total": 53,
                  "digitalized_count": 18,
                  "un_digitalized_count": 35,
                  "region_id": 1,
                  "station_type": "agnkc",
                  "code": "10",
                  "region_name": "TASHKENT CITY  "
                }
              ]
        ],
          "operation_total": {
            "total": 622001418465.76,
            "total_volume": 264982460748030.03
          },
          "station_total": [
            {
              "is_digitalized": false,
              "total": 611
            },
            {
              "is_digitalized": true,
              "total": 338
            }
          ]
        }
    """

    for value in response:
        for field in important_fields:
            assert value[field] is not None, f"Field '{value[field]}' is missing"
