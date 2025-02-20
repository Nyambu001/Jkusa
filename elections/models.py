from django.db import models
from django.core.exceptions import ValidationError
from embed_video.fields import EmbedVideoField

class YouTubeVideo(models.Model):
    video_url = EmbedVideoField()
    transcript = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Blog(models.Model):
    name = models.CharField(max_length=200, null=True)
    about = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, blank=True)
    gif = models.ImageField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not self.image and not self.gif:
            raise ValidationError("You must upload either an image or a GIF.")

    def __str__(self):
        return self.name


class Advertisement(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(blank=True, null=True)
    video = models.FileField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



