from django.shortcuts import render

from items_app.models import Item, Price


def index(request):
    items = Item.objects.all()
    objects = []
    for item in items:
        price = Price.objects.filter(item_id=item.id)[0]
        objects.append([item, price])
    return render(request, "items_app/index.html", {"objects": objects})


def item(request, item_id: int):
    item = Item.objects.get(id=item_id)
    price = Price.objects.filter(item_id=item.id)[0]
    return render(request, "items_app/item.html", {"item": item, "price": price})
