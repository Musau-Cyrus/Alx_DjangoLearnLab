from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # fields to show in list view
    list_filter = ('publication_year', 'author')  # filters on the sidebar
    search_fields = ('title', 'author')  # search box fields

admin.site.register(Book, BookAdmin)
