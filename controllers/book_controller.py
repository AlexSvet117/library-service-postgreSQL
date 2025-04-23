from flask import Blueprint, jsonify, request
from services.book_service import BookService


book_bp = Blueprint("books", __name__, url_prefix="/v2")


@book_bp.route("/books", methods = ["GET"])
def get_books():
    books = BookService.get_all_books()
    return jsonify([book.to_dict() for book in books])

@book_bp.route("/books/<string:book_id>", methods = ["GET"])
def get_book(book_id):
    book = BookService.get_book_by_id(book_id)
    if book:
        return jsonify(book.to_dict())
    return jsonify({"error" : "Book not found"}), 404


@book_bp.route("/books", methods = ["POST"])
def add_book():
    data = request.json
    if not data:
        return jsonify({"error": "The payload can not be empty"}), 400
    books = BookService.create_book(data)
    if not isinstance(books, list):
        return jsonify(books), 400
    response = {"message" : "Book succesfully created",
                "books" : [book.to_dict() for book in books]}
    return jsonify(response)


@book_bp.route("/books/<string:book_id>", methods = ["DELETE"])
def delete_book(book_id):
    result, books = BookService.delete_book(book_id)
    
    if not result:
        return jsonify({"error": " Book not found"}), 404
    response = {"message" : f"Book with book id {book_id} sucessfully deleted",
                "books": [book.to_dict() for book in books]}
    return jsonify(response)


@book_bp.route("/books/<string:book_id>", methods=["PUT"])
def update_book(book_id):
    data = request.json
    if not data:
        return jsonify({"error": "The payload cannot be empty"}), 400
    
    updated_book = BookService.update_book(book_id, data)
    
    if isinstance(updated_book, dict) and "error" in updated_book:
        return jsonify(updated_book), 400
    
    return jsonify(updated_book.to_dict())

@book_bp.route("/books/stats", methods=["GET"])
def books_stats():
    """
    Function returns statistics of existing list of books:
    - Total number of books in the library
    - Number of books by read status
    - Average rating across all books
    - Books count by genre
    """
    total_books = 0
    read = 0
    reading = 0
    to_read = 0
    total_rating = 0.0
    avg_rating = 0.0
    genre_counts = {}

    books = BookService.get_all_books()

    for book in books:
        total_books += 1
        total_rating += book.rating

        genre = book.genre if book.genre else "Unknown"
        if genre in genre_counts:
            genre_counts[genre] += 1
        else:
            genre_counts[genre] = 1

        if book.read_status == "read":
            read += 1
        elif book.read_status == "to-read":
            to_read += 1
        elif book.read_status == "reading":
            reading += 1

    if total_books > 0:
        avg_rating = total_rating / total_books
    else:
        avg_rating = 0

    return jsonify({
        "status": "The stats are calculated",
        "total_books": total_books,
        "read": read,
        "reading": reading,
        "to-read": to_read,
        "average_rating": avg_rating,
        "genre_counts": genre_counts
    }), 200