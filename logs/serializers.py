from rest_framework import serializers
from .models import ActivityLog, ActivityType, ProgressTracker, UserSession

# Serializer for ActivityType
class ActivityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityType
        fields = '__all__'

# Serializer for ActivityLog
class ActivityLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityLog
        fields = '__all__'

# Serializer for ProgressTracker
class ProgressTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgressTracker
        fields = '__all__'

# Serializer for UserSession
class UserSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSession
        fields = '__all__'
