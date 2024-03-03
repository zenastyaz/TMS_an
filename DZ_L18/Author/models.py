from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
    author: Mapped["Author"] = relationship("Author", back_populates="books")

    def __str__(self):
        return f"Book ID: {self.id} Book name: {self.name} Author name: {self.author.name}"


class Author(Base):
    __tablename__ = "authors"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    books: Mapped[List[Book]] = relationship("Book", back_populates="author", cascade="all, delete-orphan")

    def __str__(self):
        return f"Author ID: {self.id}Author name: {self.name}"


class CreateUser(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    password: Mapped[str]

    def __str__(self):
        return f": {self.id}: {self.email}"
