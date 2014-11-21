from rest_framework import viewsets

from books.models import Author, Book
from books.serializers import BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    model = Author

class BookViewSet(viewsets.ModelViewSet):
    model = Book
    serializer_class = BookSerializer