from django.contrib import admin
from django.utils.safestring import mark_safe
from blog.models import MyModel


class MyModelAdmin(admin.ModelAdmin):
    list_display = ("id", "html_preview")

    def html_preview(self, obj):
        """HTMLをプレビューする機能"""
        return mark_safe(obj.content)

    html_preview.short_description = "HTMLプレビュー"


admin.site.register(MyModel, MyModelAdmin)
