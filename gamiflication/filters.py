# filters.py
import django_filters
from .models import GameCategory, Game, GameSession, UserPerformance, UserGoal, Recommendation

class GameCategoryFilter(django_filters.FilterSet):
    class Meta:
        model = GameCategory
        fields = ['name', 'description']

class GameFilter(django_filters.FilterSet):
    class Meta:
        model = Game
        fields = ['title', 'category', 'difficulty']

class GameSessionFilter(django_filters.FilterSet):
    class Meta:
        model = GameSession
        fields = ['user', 'game']

class UserPerformanceFilter(django_filters.FilterSet):
    class Meta:
        model = UserPerformance
        fields = ['user', 'game_category']

class UserGoalFilter(django_filters.FilterSet):
    class Meta:
        model = UserGoal
        fields = ['user']

class RecommendationFilter(django_filters.FilterSet):
    class Meta:
        model = Recommendation
        fields = ['user', 'game_category', 'recommended_game']
