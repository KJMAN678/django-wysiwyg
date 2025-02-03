from django.contrib import admin
from blog.models import MyModel
from django_quill.fields import QuillFormField
from django.db import models


class MyModelAdmin(admin.ModelAdmin):
    list_display = ("id",)

    formfield_overrides = {
        models.TextField: {"widget": QuillFormField()},
    }

    class Media:
        css = {
            "all": ("admin/css/style.css",)  # カスタムCSS適用
        }


admin.site.register(MyModel, MyModelAdmin)
