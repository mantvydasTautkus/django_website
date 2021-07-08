from typing import Type
from django.contrib import admin
from .models import ItemKind, Product, Smiths

admin.site.register(Product)
admin.site.register(Smiths)
admin.site.register(ItemKind)

