from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import LoginSystem, StudentProfile, TeacherProfile, AdminProfile

# Helper function to validate file size
def validate_file_size(file):
    max_file_size = 5 * 1024 * 1024  # 5MB limit
    if file.size > max_file_size:
        raise ValidationError(f"File size must be under 5MB. Current size: {file.size / (1024 * 1024):.2f}MB")

class LoginSystemSerializer(serializers.ModelSerializer):
    # Mark access_token and refresh_token as read-only
    access_token = serializers.ReadOnlyField()
    refresh_token = serializers.ReadOnlyField()

    class Meta:
        model = LoginSystem
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'role', 'access_token', 'refresh_token']

    # Field-level validation for username
    def validate_username(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Username must be at least 5 characters long.")
        return value

    # Field-level validation for email
    def validate_email(self, value):
        if "@" not in value:
            raise serializers.ValidationError("Enter a valid email address.")
        return value

    # Field-level validation for phone_number
    def validate_phone_number(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Phone number must contain only digits.")
        if len(value) != 10:
            raise serializers.ValidationError("Phone number must be exactly 10 digits.")
        return value


class StudentProfileSerializer(serializers.ModelSerializer):
    user = LoginSystemSerializer(read_only=True)  # Nested serializer for user data

    class Meta:
        model = StudentProfile
        fields = [
            'id', 'user', 'grade', 'school_name', 'profile_picture',
            'points', 'badges', 'streak', 'games_played', 'average_score', 'accuracy_rate'
        ]

    # Field-level validation for grade (assumed to be a string, so modify accordingly if it's an integer)
    def validate_grade(self, value):
        if not value.isdigit() or int(value) < 1 or int(value) > 12:
            raise serializers.ValidationError("Grade must be a number between 1 and 12.")
        return value

    # Field-level validation for school_name
    def validate_school_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("School name must be at least 3 characters long.")
        return value

    # Validate profile picture size (custom validation)
    def validate_profile_picture(self, value):
        if value:
            validate_file_size(value)  # Call custom validator
        return value

    # Additional validation for badges (ensure it's a list of strings)
    def validate_badges(self, value):
        if not isinstance(value, list) or not all(isinstance(badge, str) for badge in value):
            raise serializers.ValidationError("Badges must be a list of strings.")
        return value

    # Custom validation for accuracy_rate to ensure it's a percentage between 0 and 100
    def validate_accuracy_rate(self, value):
        if value < 0 or value > 100:
            raise serializers.ValidationError("Accuracy rate must be between 0 and 100.")
        return value

class TeacherProfileSerializer(serializers.ModelSerializer):
    user = LoginSystemSerializer(read_only=True)  # Nested serializer for user data

    class Meta:
        model = TeacherProfile
        fields = [
            'id', 'user', 'department', 'profile_picture',
            'points', 'badges', 'streak', 'games_played', 'average_score', 'accuracy_rate'
        ]

    # Field-level validation for department
    def validate_department(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Department name must be at least 3 characters long.")
        return value

    # Validate profile picture size (custom validation)
    def validate_profile_picture(self, value):
        if value:
            validate_file_size(value)  # Call custom validator
        return value

    # Additional validation for badges (ensure it's a list of strings)
    def validate_badges(self, value):
        if not isinstance(value, list) or not all(isinstance(badge, str) for badge in value):
            raise serializers.ValidationError("Badges must be a list of strings.")
        return value

    # Custom validation for accuracy_rate to ensure it's a percentage between 0 and 100
    def validate_accuracy_rate(self, value):
        if value < 0 or value > 100:
            raise serializers.ValidationError("Accuracy rate must be between 0 and 100.")
        return value


class AdminProfileSerializer(serializers.ModelSerializer):
    user = LoginSystemSerializer(read_only=True)  # Nested serializer

    class Meta:
        model = AdminProfile
        fields = ['id', 'user', 'department', 'profile_picture']

    # Field-level validation for department
    def validate_department(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Department name must be at least 3 characters long.")
        return value

    # Validate profile picture size
    def validate_profile_picture(self, value):
        validate_file_size(value)
        return value
