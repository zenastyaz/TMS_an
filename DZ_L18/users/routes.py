from users import users_b
from users.func_bd import authorization, registration, new_email
from flask import render_template, request, flash, redirect, url_for
from utils import check_email
from flask_login import logout_user
import re


@users_b.route('/registration', methods=["POST", "GET"])
def f_registration():
    errors = []
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        if not check_email(email):
            errors.append("Некорректный адрес электронной почты.")
        if new_email(email) is not None:
            errors.append("Такой пользователь уже существует")

        if password != password2:
            errors.append('Ошибка: пароли не совпадают. Попробуйте снова.')
        if len(password) < 6:
            errors.append("Длина пароля должна быть не менее 6 символов.")
        if not re.search('[a-z]', password):
            errors.append("Пароль должен содержать хотя бы одну строчную букву.")
        if not re.search("[A-Z]", password):
            errors.append("Пароль должен содержать хотя бы одну заглавную букву.")
        if not re.search("[0-9]", password):
            errors.append("Пароль должен содержать хотя бы одну цифру.")

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
