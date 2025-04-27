from db import get_db
from psycopg2.extras import RealDictCursor

class BookRepository:
    @staticmethod
    def get_all_books():
        connection = get_db()
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("select id, book_id, title, author, publication_year, genre, read_status, rating, notes from books")
            return cursor.fetchall()
        
    @staticmethod
    def get_book_by_id(book_id):
        connection = get_db()
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("select * from books where book_id = %s;", (book_id,))
            return cursor.fetchone()
        
    @staticmethod
    def create_book(book):
        connection = get_db()
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("""insert into books(book_id,title,author, publication_year,genre,read_status,rating,notes)
                values (%s, %s,%s,%s,%s,%s,%s,%s)
                returning * 
                """, (
                book.book_id, 
                book.title, 
                book.author, 
                book.publication_year, 
                book.genre, 
                book.read_status, 
                book.rating, 
                book.notes))
            connection.commit()
            return cursor.fetchone()
    
    @staticmethod
    def delete_book(book_id):
        connection = get_db()
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("delete from books where book_id = %s returning *;", (book_id,))
            deleted = cursor.fetchone()
            connection.commit()
            return deleted
        
    @staticmethod
    def update_book_by_id(book, book_id):
        connection = get_db()
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("""update books set title = %s, author = %s, publication_year = %s, genre = %s, read_status = %s, rating = %s, notes = %s
                where book_id = %s
                returning * 
                """, (
                book.title, 
                book.author, 
                book.publication_year, 
                book.genre, 
                book.read_status, 
                book.rating, 
                book.notes,
                book_id))
            connection.commit()
            return cursor.fetchone()