from django.db import models
from django.conf import settings  # To link with the custom user model
from django.utils import timezone

# Model to track user points
class UserPoints(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='points')
    points = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.points} points'

    def add_points(self, amount):
        self.points += amount
        self.save()

# Model for badges
class Badge(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.ImageField(upload_to='badges/icons/')  # Optional icon for the badge
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

# Model to track which badges a user has earned
class UserBadge(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='badges')
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    earned_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} earned {self.badge.name}'

# Model to track user levels
class UserLevel(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='level')
    level = models.PositiveIntegerField(default=1)
    experience_points = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - Level {self.level}'

    def add_experience(self, exp):
        self.experience_points += exp
        # Logic to level up based on experience points
        while self.experience_points >= self.points_needed_for_next_level():
            self.level += 1
            self.experience_points -= self.points_needed_for_next_level()
        self.save()

    def points_needed_for_next_level(self):
        # Example: Points required for next level increases with level
        return 100 * self.level
