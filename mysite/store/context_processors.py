# -*- coding: utf-8 -*-
from models import Category


def category_list(request):
    categories = list(Category.objects.all())

    def search_child(all_categories, parent):
        all_child = {}
        for category in all_categories:
            if parent.id == category.parent_id:
                all_child.update({category: search_child(all_categories, category)})
        return all_child

    category_tree = {category: search_child(categories, category) for category in categories if not category.parent_id}
    return {"categories": category_tree}

