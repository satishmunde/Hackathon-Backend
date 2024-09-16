from rest_framework import viewsets, permissions
from .models import Community, CommunityMembership, Post, Comment, Like, ModerationAction
from .serializers import CommunitySerializer, CommunityMembershipSerializer, PostSerializer, CommentSerializer, LikeSerializer, ModerationActionSerializer

# Community ViewSet
class CommunityViewSet(viewsets.ModelViewSet):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

# CommunityMembership ViewSet
class CommunityMembershipViewSet(viewsets.ModelViewSet):
    queryset = CommunityMembership.objects.all()
    serializer_class = CommunityMembershipSerializer
    permission_classes = [permissions.IsAuthenticated]

# Post ViewSet
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# Comment ViewSet
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# Like ViewSet
class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

# ModerationAction ViewSet
class ModerationActionViewSet(viewsets.ModelViewSet):
    queryset = ModerationAction.objects.all()
    serializer_class = ModerationActionSerializer
    permission_classes = [permissions.IsAuthenticated]
