from django.db import models
from datetime import datetime

class Author(models.Model):
    """
    Represents an author of one or more books.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Represents a book written by an author.
    Each book is linked to a single author (One-to-Many relationship).
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"


