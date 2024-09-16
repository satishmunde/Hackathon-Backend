from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LectureViewSet, ShortVideosViewSet,PlaylistViewSet


router = DefaultRouter()
router.register(r'lectures', LectureViewSet)
router.register(r'Shortvideos', ShortVideosViewSet)
router.register(r'playlists', PlaylistViewSet)


urlpatterns = [
    path('', include(router.urls)),
]


