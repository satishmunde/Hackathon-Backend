from rest_framework import serializers
from .models import Lecture,  ShortVideos, Playlist

class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ['id', 'title', 'description', 'video_file', 'duration', 'upload_date']


class PlaylistSerializer(serializers.ModelSerializer):
    lectures = LectureSerializer(many=True, read_only=True)
    class Meta:
        model = Playlist
        fields = ['id', 'name', 'description', 'lectures', 'created_at']


class ShortVideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortVideos
        fields = ['id', 'title', 'video_file', 'description', 'upload_date']
