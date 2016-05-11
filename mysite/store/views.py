from django.shortcuts import render_to_response, get_object_or_404
from mysite.store.models import Category, Product
from mysite.store.tools import path_tree, my_paginator
from django.http import Http404


def index(request):
    parent_categories = Category.objects.filter(parent=None)
    items = Product.objects.all()
    items = my_paginator(request, items, 12)

    return render_to_response('index.html', {'items': items, 'categories': parent_categories})


def category(request, slug):
    requested_category = get_object_or_404(Category, slug=slug)
    items = Product.objects.filter(category=requested_category)
    items = my_paginator(request, items, 12)
    parent_categories = Category.objects.filter(parent=None)
    if request.path == requested_category.get_absolute_url():
        return render_to_response('index.html', {'items': items, 'categories': parent_categories,
                                            'breadcrumbs': path_tree(requested_category)})
    else:
        raise Http404


def search(request):
    parent_categories = Category.objects.filter(parent=None)
    query = request.GET.get('q')
    if 'q' in request.GET:
        items = Product.objects.filter(title__icontains=query)
        items = my_paginator(request, items, 12)

    return render_to_response('index.html', {'items': items, 'categories': parent_categories, 'q': query})


def product_page(request, pk):
    item = get_object_or_404(Product, pk=pk)
    requested_product = Category.objects.get(slug=item.category.slug)
    if request.path == item.get_absolute_url():
        return render_to_response('product_page.html', {'item': item, 'breadcrumbs': path_tree(requested_product)})
    else:
        raise Http404
