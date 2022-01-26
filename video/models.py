from django.db import models
from django.utils import timezone

class Video(models.Model):
    video_title = models.CharField(max_length=200)
    video_thumbnail = models.ImageField(blank=True, null=True, upload_to='thumbnails')
    video_file = models.FileField(upload_to='videos')
    video_posted_on = models.DateTimeField(default=timezone.now, blank=True)
    
    def __str__(self):
        return self.video_title
    