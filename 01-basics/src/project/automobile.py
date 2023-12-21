from pydantic import BaseModel, ConfigDict
from enum import Enum
import datetime


class AutomobileType(Enum):
    SEDAN = "Sedan"
    SUV = "SUV"
    COUPE = "Coupe"
    CONVERTIBLE = "Convertible"
    HATCHBACK = "Hatchback"
    WAGON = "Wagon"
    VAN = "Van"
    PICKUP_TRUCK = "Pickup Truck"
    MINIVAN = "Minivan"
    CROSSOVER = "Crossover"
    SPORTS_CAR = "Sports Car"
    HYBRID = "Hybrid"
    ELECTRIC = "Electric"
    DIESEL = "Diesel"
    OTHER = "Other"


class Automobile(BaseModel):
    model_config = ConfigDict(
        use_enum_values=True,
        str_strip_whitespace=True,
        str_to_lower=True,
        coerce_numbers_to_str=True,
        validate_default=True,
        validate_assignment=True,
        extra="forbid",
    )
    manufacturer: str
    series_name: str
    type_: AutomobileType
    is_electric: bool = False
    manufactured_date: datetime.date
    base_msrp_used: float
    vin: str
    number_of_doors: int = 4
    registration_country: str | None = None
    license_plate: str | None = None
