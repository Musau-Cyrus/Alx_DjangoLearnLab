from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Author, Book

class BookApiTestCase(TestCase):
    #Unit tests for the CRUD operations and additional functionalities
    def setUp(self):

         # Setup runs before each test:
        # - Create a test user (for authenticated actions)
        # - Create an Author and Book instance
        # - Initialize API client

        self.user = User.objects.create_user(username="testuser", password="testpass123")
        self.client = APIClient()

        self.author = Author.objects.create(name="J.R.R. Tolkien")
        self.book = Book.objects.create(
            title="The Hobbit", publication_year=1937, author=self.author
        )

        self.book_list_url = "/books/"
        self.book_detail_url = f"/books/{self.book.id}/"
         
     # AUTHENTICATION TESTS

    def test_list_books_without_authentication(self):
        """Unauthenticated users should be able to view the list of books."""
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book_without_authentication(self):
        """Unauthenticated users should NOT be able to create books."""
        response = self.client.post(
            self.book_list_url,
            {"title": "LOTR", "publication_year": 1954, "author": self.author.id},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # CRUD TESTS
    def test_create_book_authenticated(self):
        """Authenticated users can create a book."""
        self.client.login(username="testuser", password="testpass123")
        response = self.client.post(
            self.book_list_url,
            {"title": "The Lord of the Rings", "publication_year": 1954, "author": self.author.id},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_retrieve_book_detail(self):
        """Retrieve a single book by ID."""
        response = self.client.get(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "The Hobbit")

    def test_update_book_authenticated(self):
        """Authenticated users can update a book."""
        self.client.login(username="testuser", password="testpass123")
        response = self.client.put(
            self.book_detail_url,
            {"title": "The Hobbit Updated", "publication_year": 1937, "author": self.author.id},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "The Hobbit Updated")

    def test_delete_book_authenticated(self):
        """Authenticated users can delete a book."""
        self.client.login(username="testuser", password="testpass123")
        response = self.client.delete(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    #FILTERING, SEARCHING and ORDERING TESTS
    def test_filter_books_by_author(self):
        """Filter books by author ID."""
        response = self.client.get(f"{self.book_list_url}?author={self.author.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "The Hobbit")

    def test_search_books_by_title(self):
        """Search books by title substring."""
        response = self.client.get(f"{self.book_list_url}?search=Hobbit")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "The Hobbit")

    def test_order_books_by_publication_year(self):
        """Order books by publication year ascending."""
        # Create a newer book
        Book.objects.create(title="Silmarillion", publication_year=1977, author=self.author)
        response = self.client.get(f"{self.book_list_url}?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        years = [book["publication_year"] for book in response.data]
        self.assertEqual(years, sorted(years))