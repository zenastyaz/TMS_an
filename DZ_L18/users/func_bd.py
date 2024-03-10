from bd.database import db
from users.model import CreateUser
from flask_login import login_user
from werkzeug.security import generate_password_hash, check_password_hash


def new_email(email):
    email_user = db.session.query(CreateUser).filter_by(email=email).first()
    return email_user


def registration(email, password):
    hashed_password = generate_password_hash(password)
    new_user = CreateUser(email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()


def authorization(email, password, remember):
    user = db.session.query(CreateUser).filter(CreateUser.email == email).first()
    if user and check_password_hash(user.password, password):
        login_user(user, remember=remember)
        return True
    return False


def l_user(user_id):
    return db.session.query(CreateUser).get(user_id)
