from django.shortcuts import render_to_response
from mysite.store.models import Category, Product
from mysite.store.my_function import my_breadcrums, my_paginator



def index(request):
    category_parent = Category.objects.filter(parent=None)
    items = Product.objects.all()
    items = my_paginator(request, items, 12)

    return render_to_response('index_1.html', {'items': items, 'category_parent': category_parent})


def category(request, category_name):
    categories = Category.objects.filter(slug=category_name)
    items = Product.objects.filter(category=categories)
    category_parent = Category.objects.filter(parent=None)
    items = my_paginator(request, items, 12)
    breadcrumbs = Category.objects.get(slug=category_name)
    my_breadcrums(breadcrumbs)

    return render_to_response('index_1.html', {'items': items, 'category_parent': category_parent,
                                               'breadcrumbs': my_breadcrums(breadcrumbs)})


def search(request):
    category_parent = Category.objects.filter(parent=None)
    query = request.GET.get('q')
    if 'q' in request.GET:
        items = Product.objects.filter(title__icontains=query)
        items = my_paginator(request, items, 12)

    return render_to_response("index_1.html", {'items': items, 'category_parent': category_parent})


