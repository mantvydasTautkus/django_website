from typing import Type
from django.contrib import admin
from .models import  product_Type, Landing_photos, Product, Smiths, GaleryItem, ProductImages, GaleryImages, Comment

admin.site.register(Comment)
admin.site.register(Landing_photos)
admin.site.register(product_Type)


class ProductImagesAdmin(admin.StackedInline):
    model = ProductImages

@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]

    class Meta:
        model = Product


class GaleryImagesAdmin(admin.StackedInline):
    model = GaleryImages

@admin.register(GaleryItem)
class PostAdmin(admin.ModelAdmin):
    inlines = [GaleryImagesAdmin]

    class Meta:
        model = GaleryItem


