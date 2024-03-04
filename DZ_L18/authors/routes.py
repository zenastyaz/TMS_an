from authors import authors_b
from authors.func_bd import show_authors, add_author, delete_author
from flask import render_template, request, flash


@authors_b.route('/authors')
def authors():
    return render_template('authors.html')


@authors_b.route('/show_authors')
def f_show_authors():
    authors = show_authors()
    return render_template('show_authors.html', authors=authors)


@authors_b.route('/add_author', methods=["POST", "GET"])
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


@authors_b.route('/delete_author', methods=["POST", "GET"])
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
