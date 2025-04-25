from db import get_db

class BookRepository:
    @staticmethod
    def get_all_books():
        connection = get_db()
        with connection.cursor() as cursor:
            cursor.execute("select id, book_id, title, author, publication_year, genre, read_status, rating, notes from books")
            rows = cursor.fetchall()
            books = []
            for row in rows: 
                book = {
                    "id": row[0],
                    "book_id": row[1], 
                    "title": row[2], 
                    "author": row[3], 
                    "publication_year": row[4], 
                    "genre": row[5], 
                    "read_status": row[6], 
                    "rating": row[7], 
                    "notes": row[8]                    
                }
                books.append(book)
        return books