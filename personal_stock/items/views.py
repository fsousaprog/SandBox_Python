from django.http import HttpResponse
from django.template import loader

from .models import Item


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def items(request):
    my_items = Item.objects.all().values()
    template = loader.get_template('all_items.html')
    context = {
        'my_items': my_items,
    }
    return HttpResponse(template.render(context, request))


def details(request, item_id):
    my_item = Item.objects.get(id=item_id)
    template = loader.get_template('details.html')
    context = {
        'my_item': my_item,
    }
    return HttpResponse(template.render(context, request))


def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits': ['Apple', 'Banana', 'Cherry'],
    }
    return HttpResponse(template.render(context, request))
