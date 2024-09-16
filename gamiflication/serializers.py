# serializers.py
from rest_framework import serializers
from .models import UserPoints, Badge, UserBadge, UserLevel

# Serializer for UserPoints
class UserPointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPoints
        fields = ['points']

# Serializer for Badge
class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = ['name', 'description', 'icon']

# Serializer for UserBadge (to show badges earned by users)
class UserBadgeSerializer(serializers.ModelSerializer):
    badge = BadgeSerializer()

    class Meta:
        model = UserBadge
        fields = ['badge', 'earned_at']

# Serializer for UserLevel
class UserLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLevel
        fields = ['level', 'experience_points']
