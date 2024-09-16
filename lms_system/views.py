from rest_framework import viewsets
from .models import Lecture ,ShortVideos,Playlist

from .serializers import LectureSerializer, ShortVideosSerializer, PlaylistSerializer


class LectureViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer


class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer


class ShortVideosViewSet(viewsets.ModelViewSet):
    queryset = ShortVideos.objects.all()
    serializer_class = ShortVideosSerializer
