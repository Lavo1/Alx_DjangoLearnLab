from django.contrib import admin
from .models import Book, Author, Library  # Add all your models here

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Library)
