from sqlalchemy.orm import Session
from init_db_tables import Book, Author, engine
from sqlalchemy.orm import joinedload


def show_books():
    with Session(engine) as session:
        books = session.query(Book).options(joinedload(Book.author)).all()
        return books


def add_book(name: str, author_id: int):
    with Session(engine) as session:
        new_book = Book(name=name, author_id=author_id)
        session.add(new_book)
        session.commit()


def update_book(book_id: int, new_name: str):
    with Session(engine) as session:
        book = session.query(Book).filter(Book.id == book_id).first()
        book.name = new_name
        session.commit()


def delete_book(book_id: int):
    with Session(engine) as session:
        book = session.query(Book).filter(Book.id == book_id).first()
        session.delete(book)
        session.commit()


def show_authors():
    with Session(engine) as session:
        authors = session.query(Author).all()
        return authors


def add_author(name: str):
    with Session(engine) as session:
        new_author = Author(name=name)
        session.add(new_author)
        session.commit()


def find_book(name: str):
    with Session(engine) as session:
        books = session.query(Book).options(joinedload(Book.author)).filter(Book.name.like(f"%{name}%")).all()
        return books
