# Project1 - we created an array of BOOKS that holds book objects and performed CRUD operations


from fastapi import Body, FastAPI

app = FastAPI()         #allows uvicorn to identify that we are creating a web app of fastapi


BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]


# GET

# get all books
@app.get("/books")
async def read_all_books():
    return BOOKS

# path parameter - get the book by the book title
@app.get("/books/{book_title}")
async def read_book(book_title : str):
   for book in BOOKS:
       if book.get('title').casefold() == book_title.casefold():            #turn to lowercase
           return book
       
# Output
#  Request URL: http://localhost:8000/books/title%20one               %20 is referred as space: the dynamic paramater given is title one
# Response body
# {
#   "title": "Title One",
#   "author": "Author One",
#   "category": "science"
# }
       

# query parameter - read the category by query
@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

# Output
#  Request URL: http://localhost:8000/books/?category=science
# Response body
# Download
# [
#   {
#     "title": "Title One",
#     "author": "Author One",
#     "category": "science"
#   },
#   {
#     "title": "Title Two",
#     "author": "Author Two",
#     "category": "science"
#   }
# ]

# path parameter and query parameter - get the author and the category
@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str,category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
        book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

# Request URL
# http://localhost:8000/books/author%20two/?category=science
# Response body
# Download
# [
#   {
#     "title": "Title Two",
#     "author": "Author Two",
#     "category": "science"
#   }
# ]



# POST
@app.post("/books/create_book")
async def create_book(new_book = Body()):
    BOOKS.append(new_book)

# Request Body{
#     "title": "Title Seven",
#     "author": "Author Two",
#     "category": "Math"
#   }
# Request URL: http://localhost:8000/books/create_book
# Response: null
# check the new book calling the get api of all books and check



# PUT
@app.put("/books/update_book")
async def update_book(updated_book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book

# Request Body{
#     "title": "Title Six",
#     "author": "Author Two",
#     "category": "History"
#   }
# Request URL
# http://localhost:8000/books
# Replaces the category of title six
# check by calling the get api of all books
            
# DELETE
@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break

# Request URL
# http://localhost:8000/books/delete_book/title%20four
# the title four record is deleted feom the books list, check by calling the all books get api
        


# ASSIGNMENT - 1. Create a new API Endpoint that can fetch all books from a specific author using either Path Parameters or Query Parameters.
        
#  Path Parameters
@app.get("/books/books_author/{book_author}")
async def get_all_books_by_author(book_author: str):
    books_of_author = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold():
            books_of_author.append(book)
    return books_of_author


# Request URL
# http://localhost:8000/books/books_author/author%20two
# Response body
# [
#   {
#     "title": "Title Two",
#     "author": "Author Two",
#     "category": "science"
#   },
#   {
#     "title": "Title Six",
#     "author": "Author Two",
#     "category": "math"
#   }
# ]

