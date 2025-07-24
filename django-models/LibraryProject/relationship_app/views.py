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

from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Login View (uses Django’s built-in LoginView)
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# Logout View (uses Django’s built-in LogoutView)
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

# Registration View (custom logic)
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in after successful registration
            return redirect('home')  # Redirect to a home or dashboard view
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

