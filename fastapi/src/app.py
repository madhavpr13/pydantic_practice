from fastapi import FastAPI, HTTPException
from books import load_books
from books import BookRequest
from starlette import status

BOOKS = load_books()

app = FastAPI()


@app.get("/")
def say_hello() -> str:
    return "Hello, World"


@app.get("/books", status_code=status.HTTP_200_OK)
async def get_books():
    return BOOKS


@app.get("/books/{isbn}", status_code=status.HTTP_200_OK)
async def get_book_id(isbn: str):
    for book_dict in BOOKS:
        if book_dict["isbn"] == isbn:
            return book_dict
    return HTTPException(status_code=404, detail="Book not found")


@app.post("/create_book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    print(f"typeof book_request: {type(book_request)}")
    new_book = book_request.model_dump()
    BOOKS.append(new_book)


@app.put("/update_book/{isbn}", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(isbn: str, book_request: BookRequest):
    for book_dict in BOOKS:
        if book_dict["isbn"] == isbn:
            book_dict.update(book_request.model_dump())
            return
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/delete_book/{isbn}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(isbn: str):
    for book_dict in BOOKS:
        if book_dict["isbn"] == isbn:
            BOOKS.remove(book_dict)
    raise HTTPException(status_code=404, detail="Book not found")

if __name__ == "__main__":
    book_request = BookRequest.model_validate(BOOKS[0])
    print(book_request.model_dump(by_alias=True))
