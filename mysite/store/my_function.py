from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def my_paginator(request, item_list, number_page):
    paginator = Paginator(item_list, number_page)
    page = request.GET.get('page', 1)
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    return items


def my_breadcrums(object):
    categories = []

    def breadcrums(category):
        categories.append(category)
        if category.parent:
            breadcrums(category.parent)
    breadcrums(object)
    return categories[::-1]


