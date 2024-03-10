from books import books_b
from books.func_bd import (show_books, add_book, update_book, delete_book,
                           find_book, show_my_books, add_my_book, delete_my_book)
from flask import render_template, request, flash, redirect, url_for
from flask_login import current_user
from users.login_required import login_required


@books_b.route('/books')
def books():
    return render_template('books.html')


@books_b.route('/show_books')
def f_show_books():
    books = show_books()
    return render_template('show_books.html', books=books)


@books_b.route('/show_book/<int:book_id>')
def f_show_book(book_id):
    books = show_books()
    current_book = None
    prev_book_id = None
    next_book_id = None

    for i, book in enumerate(books):
        if book.id == book_id:
            current_book = book
            if i > 0:
                prev_book_id = books[i-1].id
            if i < len(books) - 1:
                next_book_id = books[i+1].id
            break

    if current_book:
        return render_template('show_book.html', book=current_book,
                               prev_book_id=prev_book_id, next_book_id=next_book_id)
    else:
        return 'Книга не найдена', 404


@books_b.route('/add_book', methods=["POST", "GET"])
def f_add_book():
    name = None
    author_id = None
    from authors.func_bd import show_authors
    authors = show_authors()

    if request.method == 'POST':
        len_authors = len(show_authors())
        author_id = int(request.form['author_id'])
        if len_authors >= author_id:
            name = request.form['name']
            add_book(name, author_id)
            flash('Книга успешно добавлена', 'success')
        else:
            flash('Ошибка добавления книги. Проверьте данные.', 'error')
    return render_template('add_book.html', name=name, author_id=author_id, authors=authors)


@books_b.route('/update_book', methods=["POST", "GET"])
def f_update_book():
    new_name = None
    book_id = None
    books = show_books()

    if request.method == 'POST':
        new_name = request.form['new_name']
        book_id = int(request.form['book_id'])
        if update_book(book_id, new_name):
            flash('Книга успешно обнавлена', 'success')
        else:
            flash('Ошибка обнавления книги', 'error')
    return render_template('update_book.html', book_id=book_id, new_name=new_name, books=books)


@books_b.route('/delete_book', methods=["POST", "GET"])
def f_delete_book():
    book_id = None
    books = show_books()

    if request.method == 'POST':
        book_id = int(request.form['book_id'])
        if delete_book(book_id):
            flash('Книга успешно удалена', 'success')
        else:
            flash('Ошибка удаления книги', 'error')
    return render_template('delete_book.html', book_id=book_id, books=books)


@books_b.route('/find_book',  methods=["POST", "GET"])
def f_find_book():
    books = []
    if request.method == 'POST':
        name = request.form['name']
        books = find_book(name)
    return render_template('search.html', books=books)


@books_b.route('/my_books')
@login_required
def f_show_my_books():
    books = show_my_books()
    return render_template('my_books.html', books=books)


@books_b.route('/add_my_book/<int:book_id>')
@login_required
def f_add_my_book(book_id):
    add_my_book(current_user.id, book_id)
    return redirect(url_for('books.f_show_my_books'))



@books_b.route('/delete_my_book/<int:book_id>')
@login_required
def f_delete_my_book(book_id):
    deleted = delete_my_book(current_user.id, book_id)
    if deleted:
        updated_books = show_my_books()
        return render_template('my_books.html', books=updated_books)

