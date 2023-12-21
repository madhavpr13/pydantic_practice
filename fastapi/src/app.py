from fastapi import FastAPI
from books import load_books

BOOKS = load_books()

app = FastAPI()

@app.get("/")
def say_hello() -> str:
    return "Hello, World"

@app.get("/books")
async def get_books() -> list[dict]:
    return BOOKS


@app.get("/books/{id}")
async def get_book_id(id: int) -> dict:
    for book_dict in BOOKS:
        if book_dict["id"] == id:
            return book_dict
    return dict()

