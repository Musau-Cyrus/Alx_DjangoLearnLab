from django.db import models

class Author(models.Model):
    name = models.CharField(length = 100)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(length = 100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,related_name="name")
    
    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(length = 100)
    book = models.ManyToManyField(Book, related_name="author")
    
    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(length = 100)
    library = models.OneToOneField(Library)
    
    def __str__(self):
        return self.name