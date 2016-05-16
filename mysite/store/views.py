# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.template import RequestContext

from store.models import Category, Product
from store.tools import path_to_root, page_paginator


def index(request):
    items = Product.objects.all()
    context = {
        'items': page_paginator(request, items, 12),
    }
    return render_to_response('main.html', context, context_instance=RequestContext(request))


def category(request, slug):
    requested_category = get_object_or_404(Category, slug=slug.split('/')[-1])
    items = Product.objects.filter(category=requested_category)
    context = {
        'items': page_paginator(request, items, 12),
        'breadcrumbs': path_to_root(requested_category),
    }
    if request.path == requested_category.get_absolute_url():
        return render_to_response('main.html', context, context_instance=RequestContext(request))
    else:
        raise Http404


def search(request):
    query = request.GET.get('q')
    items = None
    if query:
        items = Product.objects.filter(title__icontains=query)
        items = page_paginator(request, items, 12)
        query = u'{}{}'.format('q=', query)

    context = {
        'items': items,
        'query': query,
    }
    return render_to_response('main.html', context, context_instance=RequestContext(request))


def product_page(request, slug):
    item = get_object_or_404(Product, slug=slug)
    category_item = Category.objects.get(slug=item.category.slug)
    context = {
        'item': item,
        'breadcrumbs': path_to_root(category_item),
    }
    if request.path == item.get_absolute_url():
        return render_to_response('product_page.html', context)
    else:
        raise Http404

