from bd.database import db
from books.model import Book
from authors.model import Author


def populate_db():
    with db.session.begin():
        if db.session.query(Author).count() == 0:
            authors_list = [
                Author(name='Tolstoy'),
                Author(name='Dostoevsky'),
                Author(name='Chekhov'),
                Author(name='Pushkin')
            ]
            db.session.add_all(authors_list)
            db.session.commit()

        if db.session.query(Book).count() == 0:
            books_list = [
                Book(name='War and Peace', author_id=1),
                Book(name='Anna Karenina', author_id=1),
                Book(name='Crime and Punishment', author_id=2),
                Book(name='The Idiot', author_id=2),
                Book(name='The Cherry Orchard', author_id=3),
                Book(name='Eugene Onegin', author_id=4)
            ]
            db.session.add_all(books_list)
            db.session.commit()


populate_db()
