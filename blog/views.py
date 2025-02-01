from django.http import HttpResponse
from blog.models import MyModel

from django.utils.safestring import mark_safe


def preview(request, pk):
    mymodel = MyModel.objects.get(id=pk)
    html = f"""
    <html lang="ja">
    <title>テスト</title>
    <head>
    <style type="text/css"> {mark_safe(mymodel.css)} </style>
    </head>
    <body>{mark_safe(mymodel.content)}</body>
    </html>
    """
    return HttpResponse(html)
