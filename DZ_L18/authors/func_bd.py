from bd.database import db
from books.model import Book
from authors.model import Author


def show_authors():
    authors = db.session.query(Author).all()
    return authors


def add_author(name):
    new_author = Author(name=name)
    db.session.add(new_author)
    db.session.commit()


def delete_author(author_id):
    author = db.session.query(Author).filter(Author.id == author_id).first()
    if author:
        books = db.session.query(Book).filter(Book.author_id == author_id).all()
        for book in books:
            db.session.delete(book)
        db.session.delete(author)
        db.session.commit()
        return True
    else:
        return False
