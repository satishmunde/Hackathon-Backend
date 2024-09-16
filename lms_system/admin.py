from django.contrib import admin
from .models import Lecture, Playlist, ShortVideos

@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'upload_date')
    search_fields = ('title',)



@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    filter_horizontal = ('lectures',)



@admin.register(ShortVideos)
class ShortVideosAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_date')
    search_fields = ('title',)
