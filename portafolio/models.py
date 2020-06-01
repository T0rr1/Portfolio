from django.db import models
from django.utils import timezone


class Project(models.Model):
    title = models.CharField(max_length=100)
    summary = models.CharField(
        max_length=200, default="This project was very interesting but challenging"
    )
    description = models.TextField()
    link = models.URLField(max_length=128, default="http://github.io")
    date_posted = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to="images/", default="/zelda.jpg")

    def __str__(self):
        return self.title
