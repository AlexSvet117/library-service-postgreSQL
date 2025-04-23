class Book: 
    def __init__(self, book_id, title, author, publication_year = 0, genre = "", read_status = "to-read", rating = 0.0, notes = ""):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.genre = genre
        self.read_status = read_status
        self.rating = rating
        self.notes = notes

    def to_dict(self):
        return { 
            "book_id" : self.book_id,
            "title" : self.title,
            "author" : self.author,
            "publication_year" : self.publication_year,
            "genre" : self.genre,
            "read_status" : self.read_status,
            "rating" : self.rating,
            "notes" : self.notes
            }