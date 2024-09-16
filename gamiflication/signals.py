# In signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post, UserPoints

@receiver(post_save, sender=Post)
def reward_points_for_post(sender, instance, created, **kwargs):
    if created:
        # Reward 10 points for creating a post
        user_points, _ = UserPoints.objects.get_or_create(user=instance.author)
        user_points.add_points(10)
