from sqlalchemy.orm import Session
from bd.connection import engine
from bd.models import CreateUser
from flask_login import login_user
from werkzeug.security import generate_password_hash, check_password_hash


def new_email(email):
    with Session(engine) as session:
        email_user = session.query(CreateUser).filter_by(email=email).first()
        return email_user


def registration(email, password):
    with Session(engine) as session:
        hashed_password = generate_password_hash(password)
        new_user = CreateUser(email=email, password=hashed_password)
        session.add(new_user)
        session.commit()


def authorization(email, password, remember):
    with Session(engine) as session:
        user = session.query(CreateUser).filter(CreateUser.email == email).first()
        if user and check_password_hash(user.password, password):
            login_user(user, remember=remember)
            return True
    return False


def l_user(user_id):
    with Session(engine) as session:
        return session.query(CreateUser).get(user_id)
