from django.contrib import admin
from .models import *
class ProductImageInline(admin.TabularInline): model=ProductImage; extra=1
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin): list_display=('name','price','stock','brand'); list_filter=('category','brand'); search_fields=('name','article'); inlines=[ProductImageInline]
admin.site.register([Category,VehicleMake,VehicleModel,VehicleGeneration,VehicleEngine,News,Discount])
