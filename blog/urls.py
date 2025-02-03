from blog import views
from django.urls import path

urlpatterns = [
    path("form_view/", views.form_view, name="form_view"),
]
