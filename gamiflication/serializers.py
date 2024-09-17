from rest_framework import serializers
from .models import GameCategory, Game, GameSession, UserPerformance, UserGoal, Recommendation, Tag
from django.contrib.auth import get_user_model

# Import your user model (LoginSystem)
User = get_user_model()

### GameCategorySerializer
class GameCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GameCategory
        fields = ['id', 'name', 'description']  # Explicitly define only the necessary fields

    # Field-level validation for name
    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Game category name must be at least 3 characters long.")
        return value

    # Field-level validation for description
    def validate_description(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Game category description must be at least 10 characters long.")
        return value




class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']  # Define fields for the Tag model

class GameSerializer(serializers.ModelSerializer):
    category = GameCategorySerializer(read_only=True)  # Use nested serializer for category
    tags = TagSerializer(many=True, read_only=True)  # Use nested serializer for tags

    class Meta:
        model = Game
        fields = ['id', 'title', 'category', 'difficulty', 'content', 'correct_answer', 'description', 'image', 'tags']  # Include all necessary fields

    # Field-level validation for title
    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Game title must be at least 3 characters long.")
        return value

    # Field-level validation for difficulty (assuming a range of easy, medium, hard)
    def validate_difficulty(self, value):
        valid_difficulties = ['easy', 'medium', 'hard']
        if value not in valid_difficulties:
            raise serializers.ValidationError(f"Difficulty must be one of the following: {', '.join(valid_difficulties)}.")
        return value

    # Field-level validation for content (ensure it has some content)
    def validate_content(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Content must be at least 10 characters long.")
        return value

    # Field-level validation for correct_answer
    def validate_correct_answer(self, value):
        if len(value) == 0:
            raise serializers.ValidationError("Correct answer cannot be empty.")
        return value

    # Field-level validation for description
    def validate_description(self, value):
        if value and len(value) < 10:
            raise serializers.ValidationError("Description must be at least 10 characters long.")
        return value

### GameSessionSerializer
class GameSessionSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # Show username as a string
    game = GameSerializer(read_only=True)  # Use nested serializer to show game details

    class Meta:
        model = GameSession
        fields = ['id', 'user', 'game', 'date_played', 'score', 'time_taken', 'completed', 'hints_used', 'difficulty']
        read_only_fields = ['date_played', 'score']  # Make certain fields read-only

    # Field-level validation for time_taken (ensure time_taken is a positive number)
    def validate_time_taken(self, value):
        if value <= 0:
            raise serializers.ValidationError("Time taken must be a positive value.")
        return value

    # Field-level validation for difficulty (assuming a range of 1-5)
    def validate_difficulty(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Difficulty must be between 1 and 5.")
        return value

    # Field-level validation for hints_used (must be a positive integer)
    def validate_hints_used(self, value):
        if value < 0:
            raise serializers.ValidationError("Hints used cannot be a negative number.")
        return value

### UserPerformanceSerializer
class UserPerformanceSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # Show username as a string
    game_category = GameCategorySerializer(read_only=True)  # Use nested serializer for game category

    class Meta:
        model = UserPerformance
        fields = ['user', 'game_category', 'avg_score', 'total_games_played', 'avg_time_taken', 'accuracy_rate', 'difficulty_level']
        read_only_fields = ['avg_score', 'total_games_played', 'avg_time_taken', 'accuracy_rate']  # Make performance metrics read-only

    # Field-level validation for difficulty_level (ensure it's between 1 and 5)
    def validate_difficulty_level(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Difficulty level must be between 1 and 5.")
        return value

### UserGoalSerializer
class UserGoalSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # Show username as a string

    class Meta:
        model = UserGoal
        fields = ['id', 'user', 'description', 'created_at', 'target_completion_date', 'is_completed']
        read_only_fields = ['created_at']  # Mark created_at as read-only

    # Field-level validation for description (ensure description has some content)
    def validate_description(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Goal description must be at least 5 characters long.")
        return value

    # Field-level validation for target_completion_date (ensure it's not in the past)
    def validate_target_completion_date(self, value):
        if value and value < timezone.now().date():
            raise serializers.ValidationError("Target completion date cannot be in the past.")
        return value

### RecommendationSerializer
class RecommendationSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # Show username as a string
    game_category = GameCategorySerializer(read_only=True)  # Use nested serializer for category
    recommended_game = GameSerializer(read_only=True)  # Use nested serializer for game

    class Meta:
        model = Recommendation
        fields = ['user', 'game_category', 'message', 'recommended_game']

    # Field-level validation for message
    def validate_message(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Message must be at least 5 characters long.")
        return value
