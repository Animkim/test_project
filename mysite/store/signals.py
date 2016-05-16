def set_category_slug(sender, instance, *args, **kwargs):
    from pytils import translit
    slug = translit.slugify(instance.title.strip())
    if instance.slug != slug:
        instance.slug = slug
        instance.save()


def set_product_slug(sender, instance, *args, **kwargs):
    from pytils import translit
    slug = '{}_{}'.format(translit.slugify(instance.title.strip()), instance.pk)
    if instance.slug != slug:
        instance.slug = slug
        instance.save()
