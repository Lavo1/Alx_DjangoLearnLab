from django.urls import path
from .views import LibraryDetailView  # remove list_books if it's not defined
from .views import book_list_view


urlpatterns = [
    path('books/', book_list_view, name='book-list'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
]

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register_view

urlpatterns = [
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', register_view, name='register'),
]
