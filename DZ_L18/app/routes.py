from flask import render_template
from flask_login import LoginManager, current_user
from users.func_bd import l_user

from app import app

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return l_user(user_id)


@app.route('/')
def index():
    return render_template('index.html')
