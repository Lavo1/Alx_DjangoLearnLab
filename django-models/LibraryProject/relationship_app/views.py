from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

def book_list_view(request):
    books = Book.objects.all()
    output = '\n'.join([f"{book.title} by {book.author}" for book in books])
    return render(request, 'relationship_app/list_books.html', {'books': books})

from django.views.generic.detail import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # You’ll create this template
    context_object_name = 'library'

