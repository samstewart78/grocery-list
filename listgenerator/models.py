from django.db import models

# Create your models here.


class GroceryList(models.Model):
    key = models.SlugField(max_length=50, unique=True, null=False, blank=False)
    name = models.CharField(max_length=200, blank=False)
    date = models.DateField()
    total_estimated = models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Estimated Total")
    total_final = models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Final Total")
    products = models.ManyToManyField('products.Product', through='ListProducts')


class ListProducts(models.Model):
    grocerylist = models.ForeignKey(GroceryList)
    product = models.ForeignKey('products.Product')
    quantity = models.PositiveSmallIntegerField(default=1, blank=False)