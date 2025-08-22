from rest_framework import viewsets, permissions, filters
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Post, Like
from .serializers import PostSerializer
from rest_framework import status
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def feed(request):
    # Get all posts from users the current user follows
    following_users = request.user.following.all()
    posts = Post.objects.filter(author__in=following_users).order_by("-created_at")

    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        return Response({"error": "You already liked this post"}, status=status.HTTP_400_BAD_REQUEST)

    # Create notification for post author
    if post.author != request.user:
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb="liked your post",
            target=post,
            target_content_type=ContentType.objects.get_for_model(Post),
            target_object_id=post.id
        )

    return Response({"message": "Post liked"}, status=status.HTTP_201_CREATED)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def unlike_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

    try:
        like = Like.objects.get(user=request.user, post=post)
        like.delete()
        return Response({"message": "Post unliked"}, status=status.HTTP_200_OK)
    except Like.DoesNotExist:
        return Response({"error": "You have not liked this post"}, status=status.HTTP_400_BAD_REQUEST)

