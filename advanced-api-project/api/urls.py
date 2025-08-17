from django.urls import path,include
from .views import BookCreateView, BookDeleteView, BookDetailView, BookListView, BookUpdateView
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>', BookDetailView.as_view(), name='book_details'),
    path('books/create/', BookCreateView.as_view(), name='book_create'),
    path('books/update/', BookUpdateView.as_view(), name='book_update'),
    path('books/delete/', BookDeleteView.as_view(), name='book_delete'),
]