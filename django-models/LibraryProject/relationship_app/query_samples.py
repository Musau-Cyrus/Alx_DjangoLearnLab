from relationship_app.models import Author, Book, Library

# Query to get all books by a specific author
def get_all_books_by_author(name):
    author = Author.objects.get(author_name = name)
    books = author.books.all()

# Query to get all books in a specific library
def get_all_books_in_library(name):
    libary = Library.objects.get(name = libary_name)
    books = libary.books.all()