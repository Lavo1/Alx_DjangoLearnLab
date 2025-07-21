# relationship_app/views.py

from django.shortcuts import render
from .models import Book

# Function-Based View
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})
    
from django.views.generic.detail import DetailView
from .models import Library

# Class-Based View
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

