from django.contrib import admin
from stores.models import Store


class StoreAdmin(admin.ModelAdmin):
    fields = ('name', 'key'),
    search_fields = ['name', 'key']

# Register your models here.
admin.site.register(Store, StoreAdmin)
