from django.db import models

# Create your models here.


class Category(models.Model):
    key = models.SlugField(max_length=50, unique=True, null=False, blank=False)
    name = models.CharField(max_length=200, blank=False)

    def __unicode__(self):
        return self.name

    def is_food(self):
        return self.name in ['Dairy', 'Meat', 'Produce', 'Deli', 'Bakery']

    is_food.short_description = 'Is This Food?'
    is_food.boolean = True


class Product(models.Model):
    key = models.SlugField(max_length=50, unique=True, null=False, blank=False)
    name = models.CharField(max_length=200, blank=False)
    image = models.ImageField(upload_to='product-images')
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.name

