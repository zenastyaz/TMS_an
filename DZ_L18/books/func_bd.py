from sqlalchemy.orm import Session
from bd.connection import engine
from bd.models import Book, MyBook
from sqlalchemy.orm import joinedload
from flask_login import current_user


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


def find_book(name):
    with Session(engine) as session:
        books = session.query(Book).options(joinedload(Book.author)).filter(Book.name.like(f"%{name}%")).all()
        return books


def show_my_books():
    with Session(engine) as session:
        my_books = session.query(MyBook).filter(MyBook.user_id == current_user.id). \
            options(joinedload(MyBook.book).joinedload(Book.author)).all()
        return my_books


def add_my_book(user_id, book_id):
    with Session(engine) as session:
        book = session.query(MyBook).filter_by(user_id=user_id, book_id=book_id).first()
        if not book:
            new_book = MyBook(user_id=user_id, book_id=book_id)
            session.add(new_book)
            session.commit()
