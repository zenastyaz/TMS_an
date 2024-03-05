import tkinter as tk
from tkinter import simpledialog, messagebox
from func_bd import add_book, show_books, update_book, delete_book, show_authors, add_author, find_book


def gui_show_books(text_widget):
    books = show_books()
    text_widget.delete('1.0', tk.END)
    for book in books:
        text_widget.insert(tk.END, f"{book}\n")


def gui_add_book(root):

    book_name = simpledialog.askstring("Input", "Enter the book name:", parent=root)
    if not book_name:
        return

    author_id = simpledialog.askinteger("Input", "Enter the author ID:", parent=root)
    if not author_id:
        return

    add_book(book_name, author_id)
    messagebox.showinfo("Success", f"Book '{book_name}' added successfully.")


def gui_update_book(root):
    book_id_str = simpledialog.askstring("Input", "Enter the book ID", parent=root)
    if not book_id_str:
        return

    try:
        book_id = int(book_id_str)
    except ValueError:
        messagebox.showerror("Error", "Book ID must be an integer.")
        return

    new_name = simpledialog.askstring("Input", "Enter the book name:", parent=root)
    if not new_name:
        return

    update_book(book_id, new_name)
    messagebox.showinfo("Success", f"Book ID '{book_id}' updated to '{new_name}'.")


def gui_delete_book(text_widget, root):
    books = show_books()

    text_widget.delete('1.0', tk.END)
    text_widget.insert(tk.END, "List of all books and their ID:\n")
    for book in books:
        text_widget.insert(tk.END, f"ID: {book.id}, Name: {book.name}\n")
    book_id_str = simpledialog.askstring("Input", "Enter the book ID", parent=root)
    if not book_id_str:
        return

    try:
        book_id = int(book_id_str)
    except ValueError:
        messagebox.showerror("Error", "Book ID must be an integer.")
        return

    delete_book(book_id)
    messagebox.showinfo("Success", f"Book ID '{book_id}' deleted.")


def gui_show_authors(text_widget):
    authors = show_authors()
    text_widget.delete('1.0', tk.END)
    for author in authors:
        text_widget.insert(tk.END, f"{author}\n")


def gui_add_author(root):
    author_name = simpledialog.askstring("Input", "Enter the author name:", parent=root)
    if not author_name:
        return

    add_author(author_name)
    messagebox.showinfo("Success", f"Author '{author_name}' added successfully.")


def gui_find_book(text_widget, root):
    book_name = simpledialog.askstring("Input", "Enter the book name:", parent=root)
    if not book_name:
        return

    books = find_book(book_name)
    text_widget.delete('1.0', tk.END)
    if books:
        for book in books:
            text_widget.insert(tk.END, f"{book}\n")
        messagebox.showinfo("Success", f"Found '{len(books)}' books with name like '{book_name}'")
    else:
        text_widget.insert(tk.END, "No books found.\n")
        messagebox.showinfo("Not Found", "No books with this title were found.")


def gui_exit_program():
    exit()
