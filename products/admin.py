from django.contrib import admin
from .models import Product, Category, Occasion, Reviews


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'occasion',
        'price',
        'image',
        'stock',
        'is_available',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class OccasionAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class ReviewsAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'subject',
        'user',
        'star_rating',
        'updated',
        'status',

    )

    ordering = ('-updated',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Occasion, OccasionAdmin)
admin.site.register(Reviews, ReviewsAdmin)
