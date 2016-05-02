from django.db import models
from django.contrib import admin


class Category(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children')
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=70)
    image = models.ImageField(upload_to='files/media')

    class Meta:
        ordering = ('title',)

    def __unicode__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=70)
    image = models.ImageField(upload_to='files/media', blank=True)

    def __unicode__(self):
        return self.title


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

