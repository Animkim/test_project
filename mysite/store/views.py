from django.shortcuts import render_to_response
from mysite.store.models import Category, Product
from mysite.store.my_function import my_breadcrums, my_paginator
from django.http import Http404


def index(request):
    parent_categories = Category.objects.filter(parent=None)
    items = Product.objects.all()
    items = my_paginator(request, items, 12)

    return render_to_response('index_1.html', {'items': items, 'categories': parent_categories})


def category(request, slug):
    requested_category = Category.objects.get(slug=slug)
    items = Product.objects.filter(category=requested_category)
    items = my_paginator(request, items, 12)
    parent_categories = Category.objects.filter(parent=None)

    if request.path == requested_category.get_absolute_url():
        return render_to_response('index_1.html', {'items': items, 'categories': parent_categories,
                                               'breadcrumbs': my_breadcrums(requested_category)})
    else:
        raise Http404


def search(request):
    parent_categories = Category.objects.filter(parent=None)
    query = request.GET.get('q')
    if 'q' in request.GET:
        items = Product.objects.filter(title__icontains=query)
        items = my_paginator(request, items, 12)

    return render_to_response('index_1.html', {'items': items, 'categories': parent_categories, 'q': query})


def page_item(request, pk):
    item = Product.objects.get(pk=pk)
    breadcrumbs = Category.objects.get(slug=item.category.slug)
    if request.path == item.get_absolute_url():
        return render_to_response('page.html', {'item': item, 'breadcrumbs': my_breadcrums(breadcrumbs)})
    else:
        raise Http404
