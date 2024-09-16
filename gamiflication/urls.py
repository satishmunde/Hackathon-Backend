# urls.py
from django.urls import path
from .views import (
    UserProfileAPIView, AddPointsAPIView, BadgeListAPIView,
    AwardBadgeAPIView, UserLevelAPIView
)

urlpatterns = [
    # path('profile/', UserProfileAPIView.as_view(), name='user_profile'),
    path('add-points/', AddPointsAPIView.as_view(), name='add_points'),
    path('badges/', BadgeListAPIView.as_view(), name='badge_list'),
    path('award-badge/', AwardBadgeAPIView.as_view(), name='award_badge'),
    path('level/', UserLevelAPIView.as_view(), name='user_level'),
]
