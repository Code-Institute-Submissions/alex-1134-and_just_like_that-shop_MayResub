from django.contrib import admin
from .models import Category, Item


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )  


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'size',
        'vintage',
        'colour',
        'image',
    )

    ordering = ('sku',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
