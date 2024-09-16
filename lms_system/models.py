from django.db import models


# Base model for lecture videos
class Lecture(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    video_file = models.FileField(upload_to='lectures/')
    duration = models.DurationField()
    upload_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class Playlist(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    lectures = models.ManyToManyField(Lecture, related_name='playlists')
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Model for ShortVideos-like content (short videos or highlights)
class ShortVideos(models.Model):
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='ShortVideos/')
    description = models.TextField(blank=True, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
