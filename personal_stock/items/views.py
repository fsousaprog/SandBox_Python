from django.http import HttpResponse
from django.template import loader


def items(request):
    return HttpResponse(loader.get_template('home.html').render())

