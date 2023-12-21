from pydantic import BaseModel
from pydantic import ValidationError
from typing import Optional
import json


class Person(BaseModel):
    first_name: str
    last_name: str
    age: int


def create_person_from_json_string(json_str: str) -> Optional[Person]:
    try:
        return Person.model_validate_json(json_data=json_str)
    except ValidationError as ex:
        print(f"Exception occurred: {ex}")
        return None


def create_person_from_dict(person_dict) -> Optional[Person]:
    try:
        return Person.model_validate(person_dict)
    except ValidationError as ex:
        print(f"Exception occurred: {ex}")
        return None


if __name__ == "__main__":
    person_dict = {"first_name": "Isaac", "last_name": "Newton", "age": 84}
    newton = create_person_from_dict(person_dict)
    print(repr(newton))

    newton_from_json = create_person_from_json_string(json.dumps(person_dict))
    print(repr(newton_from_json))

    print(newton_from_json == newton)
