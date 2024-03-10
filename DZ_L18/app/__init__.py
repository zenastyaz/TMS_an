from flask import Flask
from app.config import Config


app = Flask(__name__)

app.config.from_object(Config)
app.secret_key = app.config['PROD_SECRET_KEY']

from bd.database import db

db.init_app(app)

from authors import authors_b

app.register_blueprint(authors_b, url_prefix='/authors')

from books import books_b

app.register_blueprint(books_b, url_prefix='/books')

from users import users_b

app.register_blueprint(users_b, url_prefix='/users')

from app.routes import *
login_manager.init_app(app)
