from django.http import HttpResponse
from blog.models import MyModel

from django.utils.safestring import mark_safe


def preview(request):
    mymodel = MyModel.objects.get(id=1)
    return HttpResponse(mark_safe(mymodel.content))
