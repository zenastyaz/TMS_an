from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from bd.database import db
from authors import model
from users.model import CreateUser


class Book(db.Model):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
    author: Mapped["model.Author"] = relationship("Author", back_populates="books")

    def __str__(self):
        return f"{self.id} {self.name} {self.author.name}"


class MyBook(db.Model):
    __tablename__ = "my_books"
    id: Mapped[int] = mapped_column(primary_key=True)
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    book: Mapped["Book"] = relationship("Book", backref="my_books")
    user: Mapped["CreateUser"] = relationship("CreateUser", backref="my_books")

    def __str__(self):
        return f"{self.id} {self.book.name} {self.book.author.name}"
