from django.urls import path
from .views import LibraryDetailView  # remove list_books if it's not defined
from .views import book_list_view


urlpatterns = [
    path('books/', book_list_view, name='book-list'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
]

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views 

urlpatterns = [
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
]

from django.urls import path
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
]
