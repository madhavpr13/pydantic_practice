from pydantic import BaseModel, ConfigDict
from pydantic import Field
from pydantic.alias_generators import to_camel
from typing import List, Dict


def load_books():
    import json

    with open("../files/books.json", "r") as f:
        books = json.load(f)
    return books


from dataclasses import dataclass


@dataclass
class Book:
    isbn: str
    title: str
    author: str
    genre: str
    description: str
    year_of_publication: int
    rating: float


class BookRequest(BaseModel):
    # model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)
    isbn: int = Field(validation_alias="ISBN", serialization_alias="ISBN")
    title: str
    author: str
    genre: str
    description: str
    year_of_publication: int
    rating: float = Field(ge=0, le=5)

    class Config:
        json_schema_extra = {
            "example": {
                "isbn": "978-3-16-148410-0",
                "title": "The Hobbit",
                "author": "J.R.R Tolkien",
                "genre": "Fantasy",
                "description": "The Hobbit, or There and Back Again is a children's fantasy novel by English author J. R. R. Tolkien.",
                "year_of_publication": 1937,
                "rating": 4.8,
            }
        }


if __name__ == "__main__":
    import json
    import random

    with open("../files/books.json", "r") as f:
        books = json.load(f)
    random_book = BookRequest.model_validate(random.choice(books))

    print(random_book.model_dump(by_alias=True))
