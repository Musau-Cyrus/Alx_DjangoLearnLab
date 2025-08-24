from rest_framework import viewsets, permissions, generics
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permisions import IsOwnerOrReadOnly
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Post, Like
from .serializers import LikeSerializer
from notifications.models import Notifications
from django.contrib.contenttypes.models import ContentType


#Post viewset
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# Comment Viewset
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("-created_at")
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# Get posts or feeds ordered by time
class FeedView(generics.ListAPIView):
    """
    Returns a feed of posts from users the current user follows.
    Ordered by creation date (newest first).
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()
        return Post.objects.filter(author__in=following_users).order_by("-created_at")
    
class LikePostView(APIView):
    permission_classes=[permissions.IsAuthenticated]

    def post(self, request, post_id):
        post=get_object_or_404(Post, id=post_id)

        #Prevent duplicate liking
        if Like.objects.filter(user=request.user, post=post).exists():
            return Response({"detail": "You already liked this post"}, status=status.HTTP_400_BAD_REQUEST)
        
        like =Like.objects.create(user=request.user, post=post)

        #Create notification
        if post.author != request.user:  # don’t notify self-like
            Notifications.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked",
                target=post,
                target_content_type=ContentType.objects.get_for_model(Post),
                target_object_id=post.id,
            )

            serializer = LikeSerializer(like)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class UnlikePostView(APIView):
    permission_classes=[permissions.IsAuthenticated]

    def post(self, request, post_id):
        post=get_object_or_404(Post,id=post_id)
        like=Like.objects.filter(user=request.user, post=post).first()

        if not like:
            return Response({"detail": "You have not liked this post"}, status=status.HTTP_400_BAD_REQUEST)
        
        like.delete()
        return Response({"detail": "Post unliked successfully"}, status=status.HTTP_200_OK) 