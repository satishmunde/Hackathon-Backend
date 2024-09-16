from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'student', StudentProfileViewSet)
router.register(r'teacher', TeacherProfileViewSet)
router.register(r'admin', AdminProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
