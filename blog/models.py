from django_prose_editor.fields import ProseEditorField
from django.db import models

class Project(models.Model):
    description = ProseEditorField()
