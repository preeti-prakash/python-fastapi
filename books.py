from fastapi import FastAPI

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

