from rest_framework import viewsets
from rest_framework.response import Response
from .models import ActivityLog, ActivityType, ProgressTracker, UserSession
from .serializers import ActivityLogSerializer, ActivityTypeSerializer, ProgressTrackerSerializer, UserSessionSerializer

# ViewSet for ActivityType
class ActivityTypeViewSet(viewsets.ModelViewSet):
    queryset = ActivityType.objects.all()
    serializer_class = ActivityTypeSerializer

# ViewSet for ActivityLog
class ActivityLogViewSet(viewsets.ModelViewSet):
    queryset = ActivityLog.objects.all()
    serializer_class = ActivityLogSerializer

# ViewSet for ProgressTracker
class ProgressTrackerViewSet(viewsets.ModelViewSet):
    queryset = ProgressTracker.objects.all()
    serializer_class = ProgressTrackerSerializer

# ViewSet for UserSession
class UserSessionViewSet(viewsets.ModelViewSet):
    queryset = UserSession.objects.all()
    serializer_class = UserSessionSerializer
