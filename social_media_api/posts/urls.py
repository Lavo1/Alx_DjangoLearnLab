from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet 
from . import views

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', views.feed, name='feed'),
    path("<int:pk>/like/", views.like_post, name="like-post"),
    path("<int:pk>/unlike/", views.unlike_post, name="unlike-post"),
]