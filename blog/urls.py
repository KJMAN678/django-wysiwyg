from blog import views
from django.urls import path, include

urlpatterns = [
    path("tinymce/", include("tinymce.urls")),
    path("preview/", views.preview, name="preview"),
]
