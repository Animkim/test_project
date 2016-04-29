from django.shortcuts import render_to_response
from mysite.store.models import Category, Product


def category(request):
    cat = Category.objects.all()
    return render_to_response('index.html', {'cats': cat})

