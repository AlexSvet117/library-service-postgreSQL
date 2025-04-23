from db import book_data

def validate_book_input(data):

    error = {}

    if not data.get("book_id"):
        error["book_id"] = "Book_id is required"
    
    if not data.get("title"):
        error["title"] = "title is required"
    
    if not data.get("author"):
        error ["author"] = "author is required"
        
    if data.get("book_id") and not isinstance(data.get("book_id"), str):
        error["book_id"] = "book_id should be str"
    
    if data.get("title") and not isinstance(data.get("title"), str):
        error["title"] = "title should be str"
    
    if data.get("author") and not isinstance(data.get("author"), str):
        error["author"] = "author should be str"

    for book in book_data:
        if book.book_id == data.get("book_id"):
            error ["book_id"] = f"book_id {data.get("book_id")} already exist"

    return error