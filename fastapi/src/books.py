from pydantic import BaseModel, ConfigDict
from pydantic import Field
from pydantic.alias_generators import to_camel
from typing import List, Dict

def load_books():
    import json
    with open("../files/books.json", "r") as f:
        books = json.load(f)
    return books

class BookRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)
    id_ : int = Field(validation_alias="id", serialization_alias="id")
    title: str
    author: str
    genre: str
    description: str
    year_of_publication: int
    rating: float


if __name__ =="__main__":
    import json
    import random
    with open("../files/books.json", "r") as f:
        books = json.load(f)
    random_book = BookRequest.model_validate(random.choice(books))

    print(random_book.model_dump(by_alias=True))
