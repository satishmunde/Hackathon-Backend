from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommunityViewSet, CommunityMembershipViewSet, PostViewSet, CommentViewSet, LikeViewSet, ModerationActionViewSet

router = DefaultRouter()
router.register(r'communities', CommunityViewSet)
router.register(r'memberships', CommunityMembershipViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'likes', LikeViewSet)
router.register(r'moderation', ModerationActionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
