from django.shortcuts import render
from .models import Book

# Create your views here.
def display_all_books(requst):
    books = Book.objects.all()
    context = { 'books': books }
    