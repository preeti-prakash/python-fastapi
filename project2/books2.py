from typing import Optional
from fastapi import  FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date

    


class BookRequest(BaseModel):
    id: Optional[int] = Field(description=  'ID is not required on create', default= None)               #it is optional, can be of type integer or None(type null)
    title: str = Field(min_length = 3)
    author: str = Field(min_length = 1)
    description: str = Field(min_length = 1, max_length = 100)
    rating: int = Field(gt=0, lt=6)
    published_date: int = Field(gt=1999, lt=2031)
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new book",
                "author": "codingwithroby",
                "description": "A new description of a book",
                "rating": 5,
                "published_date": 2024
                
            }
        }
    }


BOOKS = [
    Book(1, 'Computer Science Pro', 'codingwithroby', 'A very nice book!', 5, 2030),
    Book(2, 'Be Fast with FastAPI', 'codingwithroby', 'A great book!', 5, 2030),
    Book(3, 'Master Endpoints', 'codingwithroby', 'A awesome book!', 5, 2029),
    Book(4, 'HP1', 'Author 1', 'Book Description', 2, 2028),
    Book(5, 'HP2', 'Author 2', 'Book Description', 3, 2027),
    Book(6, 'HP3', 'Author 3', 'Book Description', 1, 2026)
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/{book_id}")
async def read_book(book_id : int = Path(gt = 0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail = 'Item not found')
        
@app.get("/books/")
async def read_book_by_rating(book_rating: int = Query(gt = 0, lt=6)):
    book_with_same_ratings = []
    for book in BOOKS:
        if book.rating == book_rating:
            book_with_same_ratings.append(book)
    return book_with_same_ratings

@app.get("/books/get_date/{book_published_date}")
async def get_books_by_date(book_published_date: int= Path(gt=1999,lt=2031)):
    books_with_same_published_date = []
    for book in BOOKS:
        if book.published_date == book_published_date:
            books_with_same_published_date.append(book)
    return books_with_same_published_date
            

@app.post("/create-book")
async def create_book(book_request : BookRequest ):
    new_book = Book(**book_request.model_dump())        
    BOOKS.append(find_book_id(new_book))


def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book


@app.put("/books/update_book")
async def update_book(book_update: BookRequest):
    book_changed=False
    new_book_update = Book(**book_update.model_dump())   
    for i in range(len(BOOKS)):
        if BOOKS[i].id == new_book_update.id:
            BOOKS[i] = new_book_update 
            book_changed = True
    if not book_changed:
        raise HTTPException(status_code=404, detail='Book not found')


@app.delete("/books/{book_id}")
async def delete_book(book_id: int = Path(gt = 0)):
    book_deleted=False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_deleted= True
            break
    if not book_deleted:
        raise HTTPException(status_code=404, detail='Book not found')