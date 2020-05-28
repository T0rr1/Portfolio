from django.db import models

# Create your models here.
class Portafolio(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


class Photo(models.Model):
    image = models.ImageField(upload_to="media/images")
