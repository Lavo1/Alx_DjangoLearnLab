from rest_framework import serializers
from .models import Author, Book
from django.utils import timezone


# Serializer for Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Include all model fields

    # Custom validation to ensure publication year is not in the future
    def validate_publication_year(self, value):
        current_year = timezone.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# Serializer for Author model with nested BookSerializer
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  
    # "many=True" means one author can have many books

    class Meta:
        model = Author
        fields = ['name', 'books']
