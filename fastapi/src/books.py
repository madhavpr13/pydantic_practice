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
    isbn: str = Field(validation_alias="isbn", serialization_alias="ISBN")
    title: str
    author: str
    genre: str
    description: str
    year_of_publication: int = Field(alias="yearOfPublication")
    rating: float = Field(ge=0, le=5)

    class Config:
        json_schema_extra = {
            "example": {
                "isbn": "978-3-16-148410-0",
                "title": "The Hobbit",
                "author": "J.R.R Tolkien",
                "genre": "Fantasy",
                "description": "The Hobbit, or There and Back Again is a children's fantasy novel by English author J. R. R. Tolkien.",
                "yearOfPublication": 1937,
                "rating": 4.8,
            }
        }

def delete_book(isbn: str, books: list[dict]) -> None:
    for book_dict in books:
        if book_dict["isbn"] == isbn:
            print(f'found book: {book_dict["isbn"]}')
            books.remove(book_dict)

if __name__ == "__main__":
    import json
    import random

    with open("../files/books.json", "r") as f:
        books = json.load(f)
    print(f'Number of books: {len(books)}')
    random_book = BookRequest.model_validate(random.choice(books))
    print(random_book.isbn)
    delete_book(random_book.isbn, books)
    print(f'Number of books: {len(books)}')
