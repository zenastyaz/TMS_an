from functools import wraps
from flask import redirect, url_for
from flask_login import current_user


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated:
            return f(*args, **kwargs)
        return redirect(url_for('users.f_authentication'))
    return decorated_function