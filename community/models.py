from django.db import models
from django.conf import settings  # Import the custom user model (AUTH_USER_MODEL)
from django.utils import timezone

# Community model - represents a group/forum
class Community(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_communities')
    created_at = models.DateTimeField(default=timezone.now)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, through='CommunityMembership', related_name='communities')

    def __str__(self):
        return self.name

# Through table for Community membership (tracks roles)
class CommunityMembership(models.Model):
    ROLE_CHOICES = (
        ('member', 'Member'),
        ('moderator', 'Moderator'),
        ('admin', 'Admin'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='member')
    joined_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('user', 'community')

# Post model - represents a post within a community
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# Comment model - represents a comment on a post
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')  # For threaded comments
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post.title}'

# Like model - represents likes on posts and comments
class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE, related_name='likes')
    comment = models.ForeignKey(Comment, null=True, blank=True, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('user', 'post', 'comment')  # Ensures a user can only like a post/comment once

# Moderator actions
class ModerationAction(models.Model):
    ACTION_CHOICES = (
        ('delete_post', 'Delete Post'),
        ('delete_comment', 'Delete Comment'),
        ('ban_user', 'Ban User'),
    )
    moderator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    action = models.CharField(max_length=50, choices=ACTION_CHOICES)
    target_post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    target_comment = models.ForeignKey(Comment, null=True, blank=True, on_delete=models.CASCADE)
    target_user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name='banned_users', on_delete=models.CASCADE)
    reason = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.action} by {self.moderator}'

