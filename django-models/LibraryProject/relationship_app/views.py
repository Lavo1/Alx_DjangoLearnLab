from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, Library
import os
from django.conf import settings

# ✅ Function-Based View: list all books
def list_books(request):
    books = Book.objects.all()

    # 🛠️ Debugging helper (prints template files to console)
    template_path = os.path.join(settings.BASE_DIR, 'relationship_app', 'templates')
    print("👀 TEMPLATE FILES I SEE:", os.listdir(template_path))

    return render(request, 'list_books.html', {'books': books})

# ✅ Class-Based View: show details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

    from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to the Library App</h1><p><a href='/books/'>View Books</a></p>")

