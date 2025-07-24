from relationship_app.models import Author, Book, Library, Librarian

# Query to get all books by a specific author
def get_all_books_by_author(name):
    try:
        author = Author.objects.get(name=author_name)

        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return f"No author found with name: {author_name}"
    
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
        librarian = Librarian.objects.get(library=library)  # required line
        return librarian.name
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return f"No librarian found for library: {library_name}"