from django.shortcuts import render_to_response
from mysite.store.models import Category, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    category = Category.objects.filter(parent=None)
    item = Product.objects.all()
    paginator = Paginator(item, 12)
    page = request.GET.get('page', 1)
    try:
        item = paginator.page(page)
    except PageNotAnInteger:
        item = paginator.page(1)
    except EmptyPage:
        item = paginator.page(paginator.num_pages)

    return render_to_response('index_1.html', {'items': item, 'categores': category})


def category(request, category_name):
    category = Category.objects.filter(slug=category_name)
    item = Product.objects.filter(category=category)
    cat = Category.objects.get(slug=category_name)
    category_parent = cat.children.all()
    return render_to_response('category_1.html', {'items': item, 'categores': category_parent})


def search(request):
    pass

