from users.func_bd import new_email
import re


def validate_email_pass(email, password, password2):
    errors = []

    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
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
    return errors
