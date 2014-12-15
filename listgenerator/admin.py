from django.contrib import admin
from listgenerator.models import GroceryList


class GroceryListAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'key', 'date']}),
        ('Totals', {'fields': ['total_estimated', 'total_final']}),
    ]
    list_display = ('name', 'key', 'total_estimated', 'total_final')
    list_filter = ['date']
    search_fields = ['name', 'key', 'date']

# Register your models here.
admin.site.register(GroceryList, GroceryListAdmin)
