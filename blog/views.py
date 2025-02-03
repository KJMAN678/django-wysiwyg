from django.http import HttpResponse
from blog.models import MyModel

from django.utils.safestring import mark_safe
from django.shortcuts import render
from .forms import QuillFieldForm


def form_view(request):
    return render(request, "form_view.html", {"form": QuillFieldForm()})
