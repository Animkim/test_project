from django.shortcuts import render_to_response
from mysite.store.models import Category, Product
from mysite.store.my_function import my_breadcrums, my_paginator
from django.http import Http404


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

    if request.path == breadcrumbs.get_absolute_url():
        return render_to_response('index_1.html', {'items': items, 'category_parent': category_parent,
                                               'breadcrumbs': my_breadcrums(breadcrumbs)})
    else:
        raise Http404


def search(request):
    category_parent = Category.objects.filter(parent=None)
    query = request.GET.get('q')
    print query
    if 'q' in request.GET:
        items = Product.objects.filter(title__icontains=query)
        items = my_paginator(request, items, 12)

    return render_to_response('index_1.html', {'items': items, 'category_parent': category_parent, 'q': query})


def page_item(request, pk):
    item = Product.objects.get(pk=pk)
    breadcrumbs = Category.objects.get(slug=item.category.slug)
    path = request.path
    url = item.get_absolute_url()
    print path, url
    if request.path == item.get_absolute_url():
        return render_to_response('page.html', {'item': item, 'breadcrumbs': my_breadcrums(breadcrumbs)})
    else:
        raise Http404
