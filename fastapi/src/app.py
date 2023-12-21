from fastapi import FastAPI
from books import load_books
from books import Book, BookRequest

BOOKS = load_books()

app = FastAPI()


@app.get("/")
def say_hello() -> str:
    return "Hello, World"


@app.get("/books")
async def get_books() -> list[dict]:
    return BOOKS


@app.get("/books/{isbn}")
async def get_book_id(isbn: str) -> dict:
    for book_dict in BOOKS:
        if book_dict["isbn"] == isbn:
            return book_dict
    return dict()


@app.post("/create_book")
async def create_book(book_request: BookRequest) -> None:
    print(f"typeof book_request: {type(book_request)}")
    new_book = book_request.model_dump()
    BOOKS.append(new_book)


if __name__ == "__main__":
    book_request = BookRequest.model_validate(BOOKS[0])
    print(book_request.model_dump(by_alias=True))
    