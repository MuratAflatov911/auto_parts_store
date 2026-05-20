from django.contrib import admin
from .models import (
    Category, Discount, News, Product, ProductImage,
    VehicleEngine, VehicleGeneration, VehicleMake, VehicleModel,
)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'brand', 'price', 'stock', 'is_popular')
    list_filter = ('category', 'brand', 'is_popular')
    search_fields = ('name', 'article', 'brand')
    prepopulated_fields = {'slug': ('name',)}
    autocomplete_fields = ('category',)
    inlines = [ProductImageInline]
    fieldsets = (
        ('Основное', {'fields': ('name', 'slug', 'category', 'brand', 'article')}),
        ('Цены и остатки', {'fields': ('price', 'old_price', 'stock', 'is_popular')}),
        ('Описание и фото', {'fields': ('description', 'image')}),
        ('Совместимость', {'fields': ('compatible_engines',)}),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')
    readonly_fields = ('created_at',)


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('title', 'percent', 'active')
    list_filter = ('active',)
    search_fields = ('title',)


@admin.register(VehicleMake)
class VehicleMakeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(VehicleModel)
class VehicleModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'make')
    list_filter = ('make',)
    search_fields = ('name',)


@admin.register(VehicleGeneration)
class VehicleGenerationAdmin(admin.ModelAdmin):
    list_display = ('name', 'model')
    list_filter = ('model__make',)
    search_fields = ('name', 'model__name')


@admin.register(VehicleEngine)
class VehicleEngineAdmin(admin.ModelAdmin):
    list_display = ('name', 'generation', 'year_from', 'year_to')
    list_filter = ('generation__model__make',)
    search_fields = ('name', 'generation__model__name')
