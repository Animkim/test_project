from django.shortcuts import render_to_response
from mysite.store.models import Category, Product


def index(request):
    item = Product.objects.all()
    category = Category.objects.filter(parent=None)
    return render_to_response('index_1.html', {'items': item, 'categores': category})


def category(request, category_name):
    category = Category.objects.filter(slug=category_name)
    item = Product.objects.filter(category=category)
    cat = Category.objects.get(slug=category_name)
    category_parent = cat.children.all()
    return render_to_response('category_1.html', {'items': item, 'categores': category_parent})
