from models.book_model import Book

book1 = Book(
        book_id = "001",
        title = "Oi Cat",
        author = "Some Author",
        publication_year = 2000,
        genre = "Kids books",
        read_status = "to-read",
        rating = 4.6,
        notes = "Quite a book to read for 7 year-olds"
    )

book2 = Book(
        book_id = "002",
        title = "Oi Frog",
        author = "Some Author",
        publication_year = 2002,
        genre = "Kids books",
        read_status = "to-read",
        rating = 4.8,
        notes = "Quite a book to read for 7 year-olds too"
    )

book_data = [book1, book2]