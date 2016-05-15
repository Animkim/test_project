from models import Category
from settings import MEDIA_URL


def category_list(request):
    parent_categories = Category.objects.filter(parent=None)
    return {"categories": parent_categories}


def media(request):
    return {"media": MEDIA_URL}