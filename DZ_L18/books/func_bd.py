from bd.database import db
from books.model import Book, MyBook
from sqlalchemy.orm import joinedload
from flask_login import current_user


def show_books():
    books = db.session.query(Book).options(joinedload(Book.author)).all()
    return books


def add_book(name, author_id):
    new_book = Book(name=name, author_id=author_id)
    db.session.add(new_book)
    db.session.commit()


def update_book(book_id, new_name):
    book = db.session.query(Book).filter(Book.id == book_id).first()
    if book:
        book.name = new_name
        db.session.commit()
        return True
    else:
        return False


def delete_book(book_id):
    book = db.session.query(Book).filter(Book.id == book_id).first()
    if book:
        db.session.delete(book)
        db.session.commit()
        return True
    else:
        return False


def find_book(name):
    books = db.session.query(Book).options(joinedload(Book.author)).filter(Book.name.like(f"%{name}%")).all()
    return books


def show_my_books():
    my_books = db.session.query(MyBook).filter(MyBook.user_id == current_user.id). \
        options(joinedload(MyBook.book).joinedload(Book.author)).all()
    return my_books


def add_my_book(user_id, book_id):
    book = db.session.query(MyBook).filter_by(user_id=user_id, book_id=book_id).first()
    if not book:
        new_book = MyBook(user_id=user_id, book_id=book_id)
        db.session.add(new_book)
        db.session.commit()


def delete_my_book(user_id, my_book_id):
    my_book = db.session.query(MyBook).filter(MyBook.user_id == user_id, MyBook.id == my_book_id).first()
    if my_book:
        db.session.delete(my_book)
        db.session.commit()
        return True
    else:
        return False
