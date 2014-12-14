from django.db import models

# Create your models here.


class Category(models.Model):
    key = models.SlugField(max_length=50, unique=True, null=False, blank=False)
    name = models.CharField(max_length=200, blank=False)
    is_food = models.BooleanField(null=False, default=False, verbose_name="Is This Food?")

    def __unicode__(self):
        return self.name


class Product(models.Model):
    key = models.SlugField(max_length=50, unique=True, null=False, blank=False)
    name = models.CharField(max_length=200, blank=False)
    image = models.ImageField(upload_to='product-images')
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.name

