# -*- coding: utf-8 -*-
from django.contrib import messages
from store.tools import path_to_root
from django.contrib import admin


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    fields = ('title', 'parent', 'image')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title',)
    fields = ('title', 'category', 'image')

