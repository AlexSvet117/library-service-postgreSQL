from db import book_data
from models.book_model import Book
from utils.validator import validate_book_input
from repositories.book_repository import BookRepository


class BookService:
    
    @staticmethod
    def get_all_books():
        books = BookRepository.get_all_books()
        if not books:
            return []
        return [Book(**b) for b in books]
    
    @staticmethod
    def get_book_by_id(book_id :str):
        book = BookRepository.get_book_by_id(book_id)
        return Book(**book) if book else None
    
    @staticmethod
    def create_book(data : dict):
        error = validate_book_input(data)

        if error:
            return error

            
        new_book = Book(
            book_id = data.get("book_id"),
            title = data.get("title"),
            author = data.get("author"),
            publication_year = data.get("publication_year", 0),
            genre = data.get("genre", ""),
            read_status = data.get("read_status", "to-read"),
            rating = data.get("rating", 0.0),
            notes = data.get("notes", "")
        )

        created_book = BookRepository.create_book(new_book)
        books = BookRepository.get_all_books()
        return [Book(**b) for b in books]


    @staticmethod
    def delete_book(book_id):
        deleted = BookRepository.delete_book(book_id)
        books = BookRepository.get_all_books()
        return True, [Book(**b) for b in books]
    

    @staticmethod
    def update_book(book_id: str, data: dict):
        book = BookService.get_book_by_id(book_id)
        
        if not book:
            return {"error": "Book not found"}
        
        book.title = data.get("title", book.title)
        book.author = data.get("author", book.author)
        book.publication_year = data.get("publication_year", book.publication_year)
        book.genre = data.get("genre", book.genre)
        book.read_status = data.get("read_status", book.read_status)
        book.rating = data.get("rating", book.rating)
        book.notes = data.get("notes", book.notes)
        
        return book