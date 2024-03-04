from flask import Flask
from bd.config import Config


app = Flask(__name__)

app.secret_key = Config.PROD_SECRET_KEY

from authors import authors_b

app.register_blueprint(authors_b, url_prefix='/authors')

from books import books_b

app.register_blueprint(books_b, url_prefix='/books')

from users import users_b

app.register_blueprint(users_b, url_prefix='/users')

from app.routes import *
login_manager.init_app(app)
