from django.db import models

# Create your models here.

class Video(models.Model):
    videoID =models.CharField(max_length=120,null=True, blank=True, default=None)
    title = models.CharField(max_length=120,null=True, blank=True, default=None)
    published = models.DateTimeField()
    description= models.CharField(max_length=120,null=True, blank=True, default=None)
    thumbUrls = models.CharField(max_length=120,null=True, blank=True, default=None)

    def __str__(self):
        return self.videoID