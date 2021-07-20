from typing import Type
from django.contrib import admin
from .models import ItemKind, Product, Smiths, GaleryItem, ProductImages, GaleryImages, Comment

admin.site.register(Smiths)
admin.site.register(ItemKind)
admin.site.register(Comment)

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


