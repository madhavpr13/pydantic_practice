from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel
from pydantic import field_serializer
from enum import Enum
from datetime import date

class AutomobileType(Enum):
    sedan = "Sedan"
    coupe = "Coupe"
    convertible = "Convertible"
    suv = "SUV"
    truck = "Truck"


class Automobile(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        validate_default=True,
        validate_assignment=True,
        str_strip_whitespace=True,
        alias_generator=to_camel
    )

    manufacturer: str
    series_name: str
    type_:  AutomobileType = Field(alias="type", serialization_alias="type")
    is_electric: bool = False
    manufactured_date: date = Field(alias="completionDate")
    base_msrp_usd: float = Field(
        validation_alias="msrpUSD",
        serialization_alias="baseMSRPUSD"
    )
    vin: str
    number_of_doors: int = Field(default=4, validation_alias="doors")
    registration_country: str | None = None
    license_plate: str | None = None

    @field_serializer("manufactured_date", when_used="json-unless-none")
    def serialize_date(self, value: date) -> str:
        return value.strftime("%Y-%m-%d")



if __name__ == "__main__":
    data_json = '''
    {
        "manufacturer": "BMW",
        "seriesName": "M4",
        "type": "Convertible",
        "isElectric": false,
        "completionDate": "2023-01-01",
        "msrpUSD": 93300,
        "vin": "1234567890",
        "doors": 2,
        "registrationCountry": "France",
        "licensePlate": "AAA-BBB"
    }
    '''

    car = Automobile.model_validate_json(data_json)
    print(car)

    expected_serialized_dict = {
        'manufacturer': 'BMW',
        'series_name': 'M4',
        'type_': AutomobileType.convertible,
        'is_electric': False,
        'manufactured_date': date(2023, 1, 1),
        'base_msrp_usd': 93300.0,
        'vin': '1234567890',
        'number_of_doors': 2,
        'registration_country': 'France',
        'license_plate': 'AAA-BBB'
    }

    print(car.model_dump_json(by_alias=True))

