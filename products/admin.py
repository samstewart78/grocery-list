from django.contrib import admin
from products.models import Category, Product


class ProductInline(admin.TabularInline):
    model = Product
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'key', 'is_food']
    inlines = [ProductInline]
    list_display = ('name', 'key', 'is_food')
    search_fields = ['name', 'key']


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'key', 'category']}),
        ('Product Image', {'fields': ['image']}),
    ]
    list_display = ('name', 'key', 'category')
    list_filter = ['category']
    search_fields = ['name', 'key']

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)


