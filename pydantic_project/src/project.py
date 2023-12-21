from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel
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
    type_:  AutomobileType
    is_electric: bool = False
    manufactured_date: date
    base_msrp_usd: float
    vin: str
    number_of_doors: int = 4
    registration_country: str | None = None
    license_plate: str | None = None

