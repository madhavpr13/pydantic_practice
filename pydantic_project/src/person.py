from pydantic import BaseModel, ConfigDict, ValidationError, Field
from pydantic.alias_generators import to_camel

class Person(BaseModel):
    model_config = ConfigDict(populate_by_name=True,
                              alias_generator=to_camel)
    first_name: str
    last_name: str | None = None
    age: int | None = None
    is_married: bool = False
    ssn: str | None = None
    type_: str = Field(alias="type", serialization_alias="type")


data_dict = {'first_name': 'John', 'lastName': 'Doe', 'age': 30, 'isMarried': True, 'ssn': '123-45-6789', "type": "person"}

m = Person.model_validate(data_dict)
print(m.model_dump(by_alias=True))
