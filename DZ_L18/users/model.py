from bd.database import db
from sqlalchemy.orm import Mapped, mapped_column
from flask_login import UserMixin


class CreateUser(db.Model, UserMixin):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    password: Mapped[str]
    is_active: Mapped[bool] = mapped_column(default=True)

    def __init__(self, email, password):
        self.email = email
        self.password_hash = password

    def __str__(self):
        return f": {self.id} {self.email}"

    def get_id(self):
        return str(self.id)

