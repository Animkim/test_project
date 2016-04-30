from django.shortcuts import render_to_response
from mysite.store.models import Category, Product


def index(request):
    item = Product.objects.all()
    category = Category.objects.order_by()[0:2]
    return render_to_response('index.html', {'items': item, 'categores': category})

