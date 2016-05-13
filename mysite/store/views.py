# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.template import RequestContext

from store.models import Category, Product
from store.tools import path_to_root, page_paginator


def index(request):
    items = Product.objects.all()
    items = page_paginator(request, items, 12)
    return render_to_response('main.html', {'items': items},
                              context_instance=RequestContext(request))


def category(request, slug):
    slug = slug.split('/')[-1]
    requested_category = get_object_or_404(Category, slug=slug)
    items = Product.objects.filter(category=requested_category)
    items = page_paginator(request, items, 12)
    if request.path == requested_category.get_absolute_url():
        return render_to_response('main.html', {'items': items, 'breadcrumbs': path_to_root(requested_category)},
                                  context_instance=RequestContext(request))
    else:
        raise Http404


def search(request):
    query = request.GET.get('q')
    if 'q' in request.GET and 'q':
        items = Product.objects.filter(title__icontains=query)
        items = page_paginator(request, items, 12)
        query = u'{}{}'.format('q=', query)
    else:
        items = None
    return render_to_response('main.html', {'items': items, 'q': query},
                              context_instance=RequestContext(request))


def product_page(request, slug):
    item = get_object_or_404(Product, slug=slug)
    requested_product = Category.objects.get(slug=item.category.slug)
    if request.path == item.get_absolute_url():
        return render_to_response('product_page.html', {'item': item, 'breadcrumbs': path_to_root(requested_product)})
    else:
        raise Http404

