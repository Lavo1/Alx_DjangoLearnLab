from django.urls import path
from .views import LibraryDetailView  # remove list_books if it's not defined
from .views import book_list_view


urlpatterns = [
    path('books/', book_list_view, name='book-list'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
]

from django.urls import path
from .views import CustomLoginView, CustomLogoutView, register_view

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
]
