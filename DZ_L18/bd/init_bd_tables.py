from sqlalchemy.orm import Session
from bd.database import db
from books.model import Book
from authors.model import Author
from bd.database import Base

from bd.connection import engine


Base.metadata.create_all(engine)


def populate_db():
    with Session(engine) as session:
        if session.query(Author).count() == 0:
            authors_list = [
                Author(name='Tolstoy'),
                Author(name='Dostoevsky'),
                Author(name='Chekhov'),
                Author(name='Pushkin')
            ]
            session.add_all(authors_list)
            session.commit()

        if session.query(Book).count() == 0:
            books_list = [
                Book(name='War and Peace', author_id=1),
                Book(name='Anna Karenina', author_id=1),
                Book(name='Crime and Punishment', author_id=2),
                Book(name='The Idiot', author_id=2),
                Book(name='The Cherry Orchard', author_id=3),
                Book(name='Eugene Onegin', author_id=4)
            ]
            session.add_all(books_list)
            session.commit()


populate_db()
