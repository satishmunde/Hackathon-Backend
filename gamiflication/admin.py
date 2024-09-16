# admin.py
from django.contrib import admin
from .models import UserPoints, Badge, UserBadge, UserLevel

@admin.register(UserPoints)
class UserPointsAdmin(admin.ModelAdmin):
    list_display = ['user', 'points']

@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at']

@admin.register(UserBadge)
class UserBadgeAdmin(admin.ModelAdmin):
    list_display = ['user', 'badge', 'earned_at']

@admin.register(UserLevel)
class UserLevelAdmin(admin.ModelAdmin):
    list_display = ['user', 'level', 'experience_points']
