from django.db import models

# Create your models here.


class Store(models.Model):
    key = models.SlugField(max_length=50, unique=True, null=True, blank=True)
    name = models.CharField(max_length=200, blank=False)
    products = models.ManyToManyField('products.Product', through='StoreProducts')

    def __unicode__(self):
        return self.name


class StoreProducts(models.Model):
    store = models.ForeignKey(Store)
    product = models.ForeignKey('products.Product')
    price = models.DecimalField(decimal_places=2, max_digits=5)