from django.db import models
from django.core.files.storage import default_storage
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_delete
from django.conf import settings

from django.db import models

class GameCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(GameCategory, on_delete=models.CASCADE)
    content = models.TextField()  # Store game data (puzzles, riddles, etc.)
    difficulty = models.CharField(max_length=10)  # easy, medium, hard
    correct_answer = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)  # Optional: A brief description of the game
    image = models.ImageField(upload_to='games/', blank=True, null=True)  # Optional: Image related to the game
    tags = models.ManyToManyField('Tag', blank=True)  # Optional: Tags for categorizing the game

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class GameSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Link to settings.AUTH_USER_MODEL for both student and teacher
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    date_played = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField()
    time_taken = models.FloatField()  # Time taken in seconds
    completed = models.BooleanField(default=False)  # Whether the game was completed or skipped
    hints_used = models.IntegerField(default=0)
    difficulty = models.CharField(max_length=10)  # easy, medium, hard

    def calculate_score(self):
        # Logic to calculate score based on hints, time taken, and difficulty
        pass

    def __str__(self):
        return f"GameSession for {self.user.username} - {self.game.title}"


class UserPerformance(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Links to either student or teacher
    game_category = models.ForeignKey(GameCategory, on_delete=models.CASCADE)
    avg_score = models.FloatField(default=0.0)
    total_games_played = models.IntegerField(default=0)
    avg_time_taken = models.FloatField(default=0.0)
    accuracy_rate = models.FloatField(default=0.0)  # Percentage of correct answers
    difficulty_level = models.CharField(max_length=10)  # Current user difficulty level for the category (easy, medium, hard)

    def update_performance(self):
        # Logic to update performance metrics based on GameSession data
        pass

    def __str__(self):
        return f"Performance of {self.user.username} in {self.game_category.name}"


class UserGoal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Linked to both student and teacher
    description = models.TextField()  # Description of the goal
    created_at = models.DateTimeField(auto_now_add=True)
    target_completion_date = models.DateTimeField()  # Deadline for goal
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Goal for {self.user.username}: {self.description}"

class Recommendation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Linked to both student and teacher
    game_category = models.ForeignKey(GameCategory, on_delete=models.CASCADE)
    message = models.TextField()  # Personalized message (e.g., "Focus on medium puzzles")
    recommended_game = models.ForeignKey(Game, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Recommendation for {self.user.username}"


