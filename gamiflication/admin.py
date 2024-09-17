from django.contrib import admin
from .models import GameCategory, Game, GameSession, UserPerformance, UserGoal, Recommendation

from django.contrib import admin
from .models import Game, GameCategory, Tag

# Register the GameCategory model
class GameCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name', 'description')
    ordering = ('name',)
    fields = ('name', 'description')
    # You can add additional configurations like list_filter, inlines, etc.

admin.site.register(GameCategory, GameCategoryAdmin)

# Register the Game model
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'difficulty', 'description', 'image')  # Adjust fields as needed
    search_fields = ('title', 'category__name', 'content', 'description', 'correct_answer')
    ordering = ('title',)
    list_filter = ('difficulty', 'category')  # Add filters to make searching easier
    readonly_fields = ('image',)  # If you want the image field to be read-only

admin.site.register(Game, GameAdmin)

# Optionally register the Tag model if you have it
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Tag, TagAdmin)
 # Orders games by title

@admin.register(GameSession)
class GameSessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'game', 'score', 'date_played', 'completed', 'hints_used')
    list_filter = ('completed', 'game__category', 'difficulty')  # Filter by completion, category, and difficulty
    search_fields = ('user__username', 'game__title')  # Search by username and game title
    ordering = ('-date_played',)  # Orders by the most recent game session
    date_hierarchy = 'date_played'  # Adds a date drill-down navigation

@admin.register(UserPerformance)
class UserPerformanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'game_category', 'avg_score', 'total_games_played', 'avg_time_taken', 'accuracy_rate', 'difficulty_level')
    list_filter = ('game_category', 'difficulty_level')  # Filter by game category and difficulty level
    search_fields = ('user__username', 'game_category__name')  # Search by username and game category name
    ordering = ('user', 'game_category')  # Orders by user and game category

@admin.register(UserGoal)
class UserGoalAdmin(admin.ModelAdmin):
    list_display = ('user', 'description', 'target_completion_date', 'is_completed', 'created_at')
    list_filter = ('is_completed', 'target_completion_date')  # Filter by completion status and target date
    search_fields = ('user__username', 'description')  # Search by username and goal description
    ordering = ('target_completion_date',)  # Orders by target completion date
    date_hierarchy = 'target_completion_date'  # Adds a date drill-down navigation

@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ('user', 'game_category', 'message', 'recommended_game')
    list_filter = ('game_category', 'recommended_game')  # Filter by game category and recommended game
    search_fields = ('user__username', 'game_category__name', 'message')  # Search by username, category, and message
    ordering = ('user', 'game_category')  # Orders by user and game category
