from blog import views
from django.urls import path, include

urlpatterns = [
    path("tinymce/", include("tinymce.urls")),
    path("preview/<int:pk>/", views.preview, name="preview"),
]
