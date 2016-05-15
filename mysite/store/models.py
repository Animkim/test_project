# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from store.tools import path_to_root
from django.db.models.signals import post_save, pre_save
from django.contrib import messages


class Category(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children')
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=70, blank=True)
    image = models.ImageField(upload_to='category_image')

    def get_absolute_url(self):
        if self.parent:
            return '{}'.format(self.parent.get_absolute_url()) + '{}/'.format(self.slug)
        else:
            return '/{}/'.format(self.slug)

    def __unicode__(self):
        return self.title

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
        return '{}{}/'.format(self.category.get_absolute_url(), self.slug)


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


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)


def set_caregory_slug(sender, instance, *args, **kwargs):
    from pytils import translit
    instance.slug = translit.slugify(instance.title.strip())
pre_save.connect(set_caregory_slug, sender=Category)


def set_product_slug(sender, instance, *args, **kwargs):
    from pytils import translit
    if not instance.slug:
        slug = translit.slugify(instance.title.strip())
        pk = instance.pk
        instance.slug = '{}_{}'.format(slug, pk)
        instance.save()
post_save.connect(set_product_slug, sender=Product)