from app import create_app
from db import get_db, close_db

def create_tables():
    app = create_app()

    with app.app_context():
        conn = get_db()
        cur = conn.cursor()
        cur.execute("""
            create table if not exists books (
                id serial primary key,
                book_id varchar(64) unique not null,
                title varchar(255) not null,
                author varchar(64),
                publication_year int not null,
                genre varchar(64),
                read_status varchar(64),
                rating NUMERIC(2, 1),
                notes text
            )
        """)
        conn.commit()
        cur.close()
        close_db()

if __name__ == "__main__":
    create_tables()
    print("V - Table successfully created")