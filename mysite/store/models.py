# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError
#
from store.admin import CategoryAdmin, ProductAdmin
from store.signals import set_category_slug, set_product_slug
from store.tools import path_to_root


class Category(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children')
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=70, blank=True)
    image = models.ImageField(upload_to='category_image')

    def get_absolute_url(self):
        if self.parent:
            return '{}{}/'.format(self.parent.get_absolute_url(), self.slug)
        else:
            return '/{}/'.format(self.slug)

    def __unicode__(self):
        return self.title

    def clean(self):
        if len(path_to_root(self)) == 4:
            raise ValidationError(u'Достигнута максимальная вложенность!')

    class Meta:
        ordering = ('title',)


class Product(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=70)
    image = models.ImageField(upload_to='item_image', blank=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '{}product/{}/'.format(self.category.get_absolute_url(), self.slug)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)


post_save.connect(set_category_slug, sender=Category)
post_save.connect(set_product_slug, sender=Product)