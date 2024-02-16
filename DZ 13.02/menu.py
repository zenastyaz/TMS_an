import tkinter as tk
from func_gui import (gui_show_books, gui_add_book, gui_update_book, gui_delete_book, gui_show_authors,
                      gui_add_author, gui_find_book, gui_exit_program)


root = tk.Tk()
root.title("Book Database")

text_widget = tk.Text(root, height=10, width=75)
text_widget.pack(pady=10)

show_books_button = tk.Button(root, text="Show Books", command=lambda: gui_show_books(text_widget))
show_books_button.pack(pady=10)

add_book_button = tk.Button(root, text="Add Book", command=lambda: gui_add_book(root))
add_book_button.pack(pady=10)

update_book_button = tk.Button(root, text="Update Book", command=lambda: gui_update_book(root))
update_book_button.pack(pady=10)

delete_book_button = tk.Button(root, text="Delete Book", command=lambda: gui_delete_book(text_widget, root))
delete_book_button.pack(pady=10)

show_authors_button = tk.Button(root, text="Show Authors", command=lambda: gui_show_authors(text_widget))
show_authors_button.pack(pady=10)

add_author_button = tk.Button(root, text="Add Author", command=lambda: gui_add_author(root))
add_author_button.pack(pady=10)

find_book_button = tk.Button(root, text="Find Book", command=lambda: gui_find_book(text_widget, root))
find_book_button.pack(pady=10)

exit_program_button = tk.Button(root, text="Exit", command=lambda: gui_exit_program())
exit_program_button.pack(pady=10)

root.mainloop()
