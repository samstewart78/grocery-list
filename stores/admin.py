from django.contrib import admin
from stores.models import Store, StoreProducts


class StoreProductsInline(admin.TabularInline):
    model = StoreProducts
    extra = 5


class StoreAdmin(admin.ModelAdmin):
    fields = ('name', 'key'),
    search_fields = ['name', 'key']
    inlines = [StoreProductsInline]

# Register your models here.
admin.site.register(Store, StoreAdmin)
