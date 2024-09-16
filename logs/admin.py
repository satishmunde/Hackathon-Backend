from django.contrib import admin
from .models import ActivityLog, ActivityType, ProgressTracker, UserSession

@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity_type', 'timestamp')
    list_filter = ('user', 'activity_type')
    search_fields = ('user__username', 'activity_type__name')

@admin.register(ActivityType)
class ActivityTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(ProgressTracker)
class ProgressTrackerAdmin(admin.ModelAdmin):
    list_display = ('user', 'task_name', 'is_completed', 'completed_at')
    list_filter = ('user', 'is_completed')
    search_fields = ('user__username', 'task_name')

@admin.register(UserSession)
class UserSessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'session_start', 'session_end')
    list_filter = ('user',)
    search_fields = ('user__username',)
