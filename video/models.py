from django.db import models

class Video(models.Model):
    video_title = models.CharField(max_length=200)
    video_thumbnail = models.ImageField(default='default.jpg', upload_to='thumbnails')
    video_file = models.FileField(upload_to='videos/%y')
    
    def __str__(self):
        return self.video_title
    