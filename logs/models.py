from django.db import models
from django.conf import settings
from django.utils import timezone

# Model to define types of activities (like login, viewing lecture, etc.)
class ActivityType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# Model to log user activity
class ActivityLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='activity_logs')
    activity_type = models.ForeignKey(ActivityType, on_delete=models.CASCADE, related_name='activity_logs')
    timestamp = models.DateTimeField(default=timezone.now)
    details = models.TextField(blank=True)  # To store extra information like page details, content viewed, etc.

    def __str__(self):
        return f'{self.user.username} - {self.activity_type.name} at {self.timestamp}'

# Model for tracking user progress, applicable for students and teachers
class ProgressTracker(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='progress')
    task_name = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    def mark_complete(self):
        self.is_completed = True
        self.completed_at = timezone.now()
        self.save()

    def __str__(self):
        return f'{self.user.username} - {self.task_name} - {"Completed" if self.is_completed else "Incomplete"}'

# This could track session-based activity (like active hours)
class UserSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sessions')
    session_start = models.DateTimeField(default=timezone.now)
    session_end = models.DateTimeField(null=True, blank=True)

    def end_session(self):
        self.session_end = timezone.now()
        self.save()

    def __str__(self):
        return f'{self.user.username} - Session from {self.session_start} to {self.session_end or "Ongoing"}'

