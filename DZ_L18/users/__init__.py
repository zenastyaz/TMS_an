from flask import Blueprint

users_b = Blueprint('users', __name__, template_folder='templates', static_folder='static')

from users.routes import *
