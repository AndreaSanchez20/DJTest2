#convert the python objects to JSON objects
from rest_framework import serializers
from bookstore.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
