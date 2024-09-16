from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'activity-types', views.ActivityTypeViewSet)
router.register(r'activity-logs', views.ActivityLogViewSet)
router.register(r'progress', views.ProgressTrackerViewSet)
router.register(r'sessions', views.UserSessionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
