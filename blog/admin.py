from django.contrib import admin
from blog.models import MyModel, MyImage

from django.utils.html import format_html


class MyModelAdmin(admin.ModelAdmin):
    list_display = ("id",)


class MyImageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "image_tag",
        "image_path",
    )
    readonly_fields = (
        "image_tag",
        "image_path",
    )

    def image_path(self, obj):
        if obj.image:
            return f"http://127.0.0.1:8000{format_html(obj.image.url)}"
        return "-"

    def image_tag(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="100" height="100" />'.format(obj.image.url)
            )
        return "-"


admin.site.register(MyModel, MyModelAdmin)
admin.site.register(MyImage, MyImageAdmin)
