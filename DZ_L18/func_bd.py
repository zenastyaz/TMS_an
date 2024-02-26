from sqlalchemy.orm import Session
from init_bd_tables import Book, Author, engine
from sqlalchemy.orm import joinedload


def show_books():
    with Session(engine) as session:
        books = session.query(Book).options(joinedload(Book.author)).all()
        return books


def add_book(name, author_id):
    with Session(engine) as session:
        new_book = Book(name=name, author_id=author_id)
        session.add(new_book)
        session.commit()


def update_book(book_id, new_name):
    with Session(engine) as session:
        book = session.query(Book).filter(Book.id == book_id).first()
        if book:
            book.name = new_name
            session.commit()
            return True
        else:
            return False


def delete_book(book_id):
    with Session(engine) as session:
        book = session.query(Book).filter(Book.id == book_id).first()
        if book:
            session.delete(book)
            session.commit()
            return True
        else:
            return False


def show_authors():
    with Session(engine) as session:
        authors = session.query(Author).all()
        return authors


def add_author(name):
    with Session(engine) as session:
        new_author = Author(name=name)
        session.add(new_author)
        session.commit()


def delete_author(author_id):
    with Session(engine) as session:
        author = session.query(Author).filter(Author.id == author_id).first()
        if author:
            books = session.query(Book).filter(Book.author_id == author_id).all()
            for book in books:
                session.delete(book)
            session.delete(author)
            session.commit()
            return True
        else:
            return False


def find_book(name):
    with Session(engine) as session:
        books = session.query(Book).options(joinedload(Book.author)).filter(Book.name.like(f"%{name}%")).all()
        return books
