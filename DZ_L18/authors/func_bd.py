from sqlalchemy.orm import Session
from bd.connection import engine
from bd.models import Author, Book


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
