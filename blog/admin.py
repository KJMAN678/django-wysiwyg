from django.contrib import admin
from django.utils.safestring import mark_safe
from blog.models import MyModel


class MyModelAdmin(admin.ModelAdmin):
    list_display = ("id", "html_preview")

    def html_preview(self, obj):
        """HTMLをプレビューする機能"""
        url = f"http://127.0.0.1:8000/blog/preview/{obj.id}/"
        return mark_safe(f"<a href={url}>{url}<a>")


admin.site.register(MyModel, MyModelAdmin)
