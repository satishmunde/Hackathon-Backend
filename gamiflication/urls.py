from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    GameCategoryViewSet, GameViewSet, GameSessionViewSet,
    UserPerformanceViewSet, UserGoalViewSet, RecommendationViewSet
)

router = DefaultRouter()
router.register(r'game-categories', GameCategoryViewSet)
router.register(r'games', GameViewSet)
router.register(r'game-sessions', GameSessionViewSet)
router.register(r'user-performances', UserPerformanceViewSet)
router.register(r'user-goals', UserGoalViewSet)
router.register(r'recommendations', RecommendationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
