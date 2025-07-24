from relationship_app.models import Author, Book, Library

# Query to get all books by a specific author
def get_all_books_by_author(name):
    try:
        author = Author.objects.get(author_name=name)
        books = author.books.all()
        return books
    except Author.DoesNotExist:
        return f"No author found with name: {name}"

# Query to get all books in a specific library
def get_all_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return books
    except Library.DoesNotExist:
        return f"No library found with name: {library_name}"

# Query to get the librarian for a specific library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian
    except Library.DoesNotExist:
        return f"No library found with name: {library_name}"
