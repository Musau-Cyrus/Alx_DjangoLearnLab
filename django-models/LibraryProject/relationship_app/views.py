from django.shortcuts import render
from .models import Book

# Create your views here.
def display_all_books(request):
    books = Book.objects.all()
    context = { 'books': books }
    return render(request, 'relationship_app/list_books.html', context)