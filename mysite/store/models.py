from django.db import models


class Category(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True)
    title = models.CharField(max_length=40)
    slug = models.SlugField(max_length=50)
    image = models.ImageField(upload_to='files/media')

    class Meta:
        ordering = ('title',)


class Product(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=40)
    slug = models.SlugField(max_length=80)
    image = models.ImageField(upload_to='files/media')
