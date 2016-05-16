from models import Category


def category_list(request):
    parent_categories = Category.objects.filter(parent=None)
    return {"categories": parent_categories}

