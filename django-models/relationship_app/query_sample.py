import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Create sample data
author = Author.objects.create(name='J.K. Rowling')
book = Book.objects.create(title='Harry Potter', author=author)
library = Library.objects.create(name='Central Library')
library.books.add(book)
librarian = Librarian.objects.create(name='John Doe', library=library)

print("Sample data created successfully.")