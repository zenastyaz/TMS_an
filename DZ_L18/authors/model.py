from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from bd.database import db
import books.model


class Author(db.Model):
    __tablename__ = "authors"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    books: Mapped[List['books.model.Book']] = relationship("Book", back_populates="author", cascade="all, delete-orphan")

    def __str__(self):
        return f"{self.id} {self.name}"