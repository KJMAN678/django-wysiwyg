from django.db import models
from tinymce.models import HTMLField


class MyModel(models.Model):
    content = HTMLField()


class MyImage(models.Model):
    image = models.ImageField(upload_to="images/", blank=True, null=True)
