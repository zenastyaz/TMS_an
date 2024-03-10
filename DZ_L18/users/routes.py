from users import users_b
from users.func_bd import authorization, registration
from flask import render_template, request, flash, redirect, url_for
from users.func_valid import validate_email_pass
from flask_login import logout_user


@users_b.route('/registration', methods=["POST", "GET"])
def f_registration():
    errors = []
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        errors.extend(validate_email_pass(email, password, password2))

        if not errors:
            registration(email, password)
            return redirect(url_for('index'))

    return render_template('registration.html', errors=errors)


@users_b.route('/authorization',  methods=["POST", "GET"])
def f_authentication():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember_me = request.form.get('remember') == 'on'
        if authorization(email, password, remember_me):
            return redirect(url_for('index'))
        else:
            flash('Неверный email или пароль.')

    return render_template('authentication.html')


@users_b.route('/logout', methods=['POST', 'GET'])
def logout():
    logout_user()
    return redirect(url_for('index'))
