from project import Automobile, AutomobileType
from pydantic import ValidationError
from datetime import date


def test_automobile(data) -> bool:
    try:
        Automobile.model_validate(data)
        return True
    except ValidationError:
        try:
            Automobile.model_validate_json(data)
            return True
        except ValidationError as ex:
            return False


if __name__ == "__main__":
    data_json = '''
    {
        "manufacturer": " BMW ",
        "series_name": " M4 ",
        "type_": "Convertible",
        "manufactured_date": "2023-01-01",
        "base_msrp_usd": 93300,
        "vin": " 1234567890 "
    }
    '''


    data_json_expected_serialization = {
        'manufacturer': 'BMW',
        'series_name': 'M4',
        'type_': AutomobileType.convertible,
        'is_electric': False,
        'manufactured_date': date(2023, 1, 1),
        'base_msrp_usd': 93300.0,
        'vin': '1234567890',
        'number_of_doors': 4,
        'registration_country': None,
        'license_plate': None
    }
    car = Automobile.model_validate_json(data_json)
    print(car.model_dump())

    expected_car = Automobile.model_validate(data_json_expected_serialization)
    print(expected_car.model_dump())

    print(car.model_dump() == data_json_expected_serialization)