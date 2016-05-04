from django.shortcuts import render_to_response, HttpResponse
from mysite.store.models import Category, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    category_parent = Category.objects.filter(parent=None)
    items = Product.objects.all()
    paginator = Paginator(items, 8)
    page = request.GET.get('page', 1)
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    return render_to_response('index_1.html', {'items': items, 'category_parent': category_parent})


def category(request, category_name):
    categories = Category.objects.filter(slug=category_name)
    items = Product.objects.filter(category=categories)
    category_parent = Category.objects.filter(parent=None)
    paginator = Paginator(items, 12)
    page = request.GET.get('page', 1)
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    return render_to_response('index_1.html', {'items': items, 'category_parent': category_parent})


def search(request):
    print 'lalalal'
    query = request.GET.get('q')
    if 'q' in request.GET:
        items = Product.objects.filter(title__icontains=query)
    return render_to_response("index_1.html", {'items': items})

