from django.db import models
from django_quill.fields import QuillField


class MyModel(models.Model):
    content = QuillField()
