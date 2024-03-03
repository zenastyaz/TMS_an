from flask import Blueprint

authors_b = Blueprint('authors', __name__, template_folder="templates")

from authors.routes import *
