from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    """
    API endpoint that provides:
    - Listing of all books
    - Filtering, Searching, and Ordering functionalities
    
    ### 🔹 Filtering
    Implemented using `DjangoFilterBackend` and `filterset_fields`.
    Allows exact matches on specific fields.

    Example requests:
    - /books/?author=1
        → Returns all books written by Author with ID 1
    - /books/?publication_year=2020
        → Returns all books published in 2020
    - /books/?title=The%20Hobbit
        → Returns books with exact title "The Hobbit"

    ### 🔹 Searching
    Implemented using `SearchFilter` and `search_fields`.
    Allows partial, case-insensitive text search.

    Example requests:
    - /books/?search=Hobbit
        → Returns books with "Hobbit" in the title or author name
    - /books/?search=Tolkien
        → Returns all books whose author name contains "Tolkien"

    ### 🔹 Ordering
    Implemented using `OrderingFilter` and `ordering_fields`.
    Users can sort results by specific fields.
    A minus sign (`-`) indicates descending order.

    Example requests:
    - /books/?ordering=title
        → Orders books alphabetically by title (A → Z)
    - /books/?ordering=-title
        → Orders books in reverse alphabetical order (Z → A)
    - /books/?ordering=publication_year
        → Orders books from oldest to newest
    - /books/?ordering=-publication_year
        → Orders books from newest to oldest

    ### 🔹 Combining Features
    Filtering, searching, and ordering can be combined in one request.
    Example:
    - /books/?search=Gatsby&ordering=-publication_year
        → Finds books with "Gatsby" in title/author and orders them newest first
    """

    #Enabling filtering, ordering and searching
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    #Fields that can be filtered
    filter_fields = ['title', 'author','publication_year']

    #Fields that can be searched
    search_fields = ['title', 'publication_year']

    #Ordering fields
    ordering_fields = ['title', 'publication_year']
    
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]