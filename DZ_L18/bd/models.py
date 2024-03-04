from sqlalchemy.orm import DeclarativeBase
from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from flask_login import UserMixin


class Base(DeclarativeBase):
    pass


class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
    author: Mapped["Author"] = relationship("Author", back_populates="books")

    def __str__(self):
        return f"{self.id} {self.name} {self.author.name}"


class Author(Base):
    __tablename__ = "authors"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    books: Mapped[List[Book]] = relationship("Book", back_populates="author", cascade="all, delete-orphan")

    def __str__(self):
        return f"{self.id} {self.name}"


class CreateUser(Base, UserMixin):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    password: Mapped[str]
    is_active: Mapped[bool] = mapped_column(default=True)

    def __str__(self):
        return f": {self.id} {self.email}"

    def get_id(self):
        return str(self.id)


class MyBook(Base):
    __tablename__ = "my_books"
    id: Mapped[int] = mapped_column(primary_key=True)
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    book: Mapped["Book"] = relationship("Book", backref="my_books")
    user: Mapped["CreateUser"] = relationship("CreateUser", backref="my_books")

    def __str__(self):
        return f"{self.id} {self.book.name} {self.book.author.name}"
