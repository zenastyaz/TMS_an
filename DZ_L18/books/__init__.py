from flask import Blueprint

books_b = Blueprint('books', __name__, template_folder='templates')

from books.routes import *
