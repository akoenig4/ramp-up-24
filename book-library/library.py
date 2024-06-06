from fastapi import FastAPI # noqa: E999
from pydantic import BaseModel
app = FastAPI()
fakeDatabase = {}
counter = 0
class Book(BaseModel):
    title: str
    author: str
    year: int
all_books = []
@app.post("/books/")
async def make_book(book: Book):
    global counter
    counter += 1
    newId = counter
    fakeDatabase[newId] = {'title':book.title, 'author':book.author, 'year':book.year}
    all_books.append(book)
    return {"id: " : newId, "book info: " : fakeDatabase[newId]}

@app.get("/books/")
async def get_all_books():
    return {'books': fakeDatabase}

@app.get("/books/{id}")
async def get_book(id: int):
    return fakeDatabase[id]

@app.put("/books/{id}")
async def put_book_details(id: int, book: Book):
    fakeDatabase[id]['title'] = book.title
    fakeDatabase[id]['author'] = book.author
    fakeDatabase[id]['year'] = book.year
    return {"id: " : id, "book info: " : fakeDatabase[id]}

@app.delete("/books/{id}")
async def delete_book(id: int):
    fakeDatabase.pop(id)
    return fakeDatabase
    
