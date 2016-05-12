# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from mysite.store.tools import path_to_root
from django.db.models.signals import pre_save


class Category(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children')
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=70, blank=True)
    image = models.ImageField(upload_to='category_image')

    def save(self, *args, **kwargs):
        if len(path_to_root(self)) == 4:
            return u'Достигнута максимальная вложенность!'
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        url = []
        path_slugs = lambda query: (query and url.append(query.slug) or (query.parent and path_slugs(query.parent)))
        path_slugs(self)
        return '/{}/'.format('/'.join(url[::-1]))

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
        return '{}{}/{}/'.format(self.category.get_absolute_url(), self.slug, self.id)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)


def set_caregory_slug(sender, instance, *args, **kwargs):
    from pytils import translit
    instance.slug = translit.slugify(instance.title.strip())


pre_save.connect(set_caregory_slug, sender=Category)