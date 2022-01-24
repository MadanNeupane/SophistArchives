from django.db import models

class Video(models.Model):
    video_title = models.CharField(max_length=200)
    video_file = models.FileField(upload_to='video/%y')
    
    def __str__(self):
        return self.video_title
    