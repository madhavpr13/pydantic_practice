from typing import Union

from automobile import Automobile
from pydantic import ValidationError


def test_automobile(data) -> Union[Automobile, None]:
    automobile = None
    try:
        automobile = Automobile.model_validate(data)
        print(f"Validation successful: {repr(automobile)}")
    except ValidationError:
        try:
            automobile = Automobile.model_validate_json(data)
            print(f"Validation successful: {repr(automobile)}")
        except ValidationError as ex:
            print(f"Validation error occurred: {ex}")
    return automobile


if __name__ == "__main__":
    data_json = {
        "manufacturer": "BMW",
        "series_name": "M4",
        "type_": "Convertible",
        "manufactured_date": "2023-01-01",
        "base_msrp_used": 100000,
        "vin": "1234567890",
    }

    automobile = Automobile.model_validate(data_json)
    print(automobile)
