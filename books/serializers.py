from rest_framework import serializers
from books.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book