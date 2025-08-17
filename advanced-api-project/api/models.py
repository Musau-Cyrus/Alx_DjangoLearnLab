from django.db import models

#Author model has one field 'name' that is used to store the author's fullname 
class Author(models.Model):
    name = models.CharField(max_length=255)

#The book model is used to represent a published book and has four field
# 'title' this is the name of the book
# 'publication_year' this fieldis used to indicate the year the book was published
# 'author' this is a foreign key to author mosel and is used to show that each book has a specificor other is linked to a specific author
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)# on_delete used to show that if an author has been deleted the the books that he/she is linked to are automatically deleted.
    