from sqlalchemy.orm import Session
from bd.init_bd_tables import Book, Author, engine
from sqlalchemy.orm import joinedload
from Author.models import CreateUser
from flask_login import login_user
from werkzeug.security import generate_password_hash, check_password_hash


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


def authorization(email, password):
    with Session(engine) as session:
        user = session.query(CreateUser).filter(CreateUser.email == email).first()
        if user and check_password_hash(user.password, password):
            remember = True
            login_user(user, remember=remember)
            return True
    return False


def registration(email, password):
    with Session(engine) as session:
        hashed_password = generate_password_hash(password)
        new_user = CreateUser(email=email, password=hashed_password)
        session.add(new_user)
        session.commit()
