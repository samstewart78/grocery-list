from django.contrib import admin
from listgenerator.models import GroceryList, ListProducts

class ListProductsInline(admin.TabularInline):
    model = ListProducts
    extra = 5


class GroceryListAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'key', 'date']}),
        ('Totals', {'fields': ['total_estimated', 'total_final']}),
    ]
    list_display = ('name', 'key', 'total_estimated', 'total_final')
    search_fields = ['name', 'key', 'date']
    list_filter = ['date']
    inlines = [ListProductsInline]

# Register your models here.
admin.site.register(GroceryList, GroceryListAdmin)
