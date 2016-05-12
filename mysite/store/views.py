from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.template import RequestContext

from mysite.store.context_processors import category_list
from mysite.store.models import Category, Product
from mysite.store.tools import path_to_root, page_paginator


def index(request):
    items = Product.objects.all()
    items = page_paginator(request, items, 12)
    return render_to_response('index.html', {'items': items},
                              context_instance=RequestContext(request, processors=[category_list]))


def category(request, slug):
    requested_category = get_object_or_404(Category, slug=slug)
    items = Product.objects.filter(category=requested_category)
    items = page_paginator(request, items, 12)
    if request.path == requested_category.get_absolute_url():
        return render_to_response('index.html', {'items': items, 'breadcrumbs': path_to_root(requested_category)},
                                  context_instance=RequestContext(request, processors=[category_list]))
    else:
        raise Http404


def search(request):
    query = request.GET.get('q')
    if 'q' in request.GET:
        items = Product.objects.filter(title__icontains=query)
        items = page_paginator(request, items, 12)
    return render_to_response('index.html', {'items': items, 'q': query},
                              context_instance=RequestContext(request, processors=[category_list]))


def product_page(request, pk):
    item = get_object_or_404(Product, pk=pk)
    requested_product = Category.objects.get(slug=item.category.slug)
    if request.path == item.get_absolute_url():
        return render_to_response('product_page.html', {'item': item, 'breadcrumbs': path_to_root(requested_product)})
    else:
        raise Http404

