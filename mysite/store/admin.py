# -*- coding: utf-8 -*-
from django.contrib import messages
from store.tools import path_to_root
from django.contrib import admin


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    fields = ('title', 'parent', 'image')

    def save_model(self, request, obj, form, change):
        if len(path_to_root(obj)) == 4:
            messages.error(request, u'Достигнута максимальная вложенность!')
        else:
            return super(CategoryAdmin, self).save_model(request, obj, form, change)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title',)
    fields = ('title', 'category', 'image')

