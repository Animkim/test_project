# -*- coding: utf-8 -*-
from models import Category


def category_list(request):
    categories = list(Category.objects.all())

    def rel(all_cat, cat_par):
        a = {}
        for cat in all_cat:
            if cat_par.id == cat.parent_id:
                a.update({cat: rel(all_cat, cat)})
        return a

    cat = {c: rel(categories, c) for c in categories if not c.parent_id}
    return {"categories": cat}

