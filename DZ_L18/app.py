from flask import Flask
from flask import render_template, request, flash
from func_bd import show_books, add_book, update_book, delete_book, show_authors, add_author, delete_author,  find_book


app = Flask(__name__)
app.secret_key = 'zxc'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/books')
def books():
    return render_template('books.html')


@app.route('/show_books')
def f_show_books():
    books = show_books()
    return render_template('show_books.html', books=books)


@app.route('/show_book/<int:book_id>')
def f_show_book(book_id):
    books = show_books()
    current_book = None
    prev_book_id = None
    next_book_id = None

    for i, book in enumerate(books):
        if book.id == book_id:  # Предполагается, что у книг есть уникальные идентификаторы
            current_book = book
            if i > 0:
                prev_book_id = books[i-1].id
            if i < len(books) - 1:
                next_book_id = books[i+1].id
            break

    if current_book:
        return render_template('show_book.html', book=current_book, prev_book_id=prev_book_id, next_book_id=next_book_id)
    else:
        return 'Книга не найдена', 404



@app.route('/add_book', methods=["POST", "GET"])
def f_add_book():
    name = None
    author_id = None
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


@app.route('/update_book', methods=["POST", "GET"])
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


@app.route('/delete_book', methods=["POST", "GET"])
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


@app.route('/authors')
def author():
    return render_template('authors.html')


@app.route('/show_authors')
def f_show_authors():
    authors = show_authors()
    return render_template('show_authors.html', authors=authors)


@app.route('/add_author', methods=["POST", "GET"])
def f_add_author():
    name = None

    if request.method == 'POST':
        name = request.form['name']
        if name:
            add_author(name)
            flash('Автор успешно добавлен', 'success')
        else:
            flash('Ошибка добавления автора. Проверьте данные.', 'error')
    return render_template('add_author.html', name=name)


@app.route('/delete_author', methods=["POST", "GET"])
def f_delete_author():
    author_id = None
    authors = show_authors()

    if request.method == 'POST':
        author_id = int(request.form['author_id'])
        if delete_author(author_id):
            flash('Автор успешно удален', 'success')
        else:
            flash('Ошибка удаления автора', 'error')
    return render_template('delete_author.html', author_id=author_id, authors=authors)


@app.route('/find_book',  methods=["POST", "GET"])
def f_find_book():
    books = []
    if request.method == 'POST':
        name = request.form['name']
        books = find_book(name)
    return render_template('search.html', books=books)


@app.route('/exit')
def f_exit():
    exit()


if __name__ == '__main___':
    app.run(debug=True)
