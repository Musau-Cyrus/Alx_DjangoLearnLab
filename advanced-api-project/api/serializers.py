from rest_framework import serializers
from .models import Book, Author
from datetime import date

# The AuthorSerializer is user to convert the author model instances into a JSON format and vice versa
# We include the author id so that the client API can use    it to refer to an auther's ID whenever needed and 'name' to see the authors name
class AuthorSerializer(serializers.ModelSerializer):

    books = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['id', 'name']

# The BookSerializer is used to handle serialization and deserialization of the author model

# Relationship handling:
# - In Django, the ForeignKey in Book to Author creates a one-to-many relationship.
# - In this serializer, we represent the author field as another serializer (AuthorSerializer) so we can show the author's details inline when returning book data.

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

     # This method validates the 'publication_year' field to ensure it is not in the future.    
    def validate_publication_year(self, value):
        current_year = date.today().year
        if (value > current_year):
            raise serializers.ValidationError("The publication year can not be in the future!")
        return value

