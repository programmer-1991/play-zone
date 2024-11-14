from django.contrib import admin
from .models import Product, Category, Game, Console, Platform

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class GameAdmin(admin.ModelAdmin):
        list_display = (
        'title',
        'platform',
        'release',
    )


class ConsoleAdmin(admin.ModelAdmin):
        list_display = (
        'title',
        'platform',
        'release',
    )

        
class PlatformAdmin(admin.ModelAdmin):
        list_display = (
        'name',
    )

admin.site.register(Game, GameAdmin)
admin.site.register(Console, ConsoleAdmin)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)