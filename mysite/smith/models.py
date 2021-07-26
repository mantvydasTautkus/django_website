from os import name
from django.core.paginator import EmptyPage
from django.db import models
from django.db.models.base import Model
from django.urls import reverse
import uuid


class Product(models.Model):
    name = models.CharField("Names", max_length=200, null=True)
    height = models.IntegerField("Height", help_text="how tall is the item in cm ", null=True)
    whith = models.IntegerField("Whith", help_text="how wide is the item in cm", null=True)
    lenght = models.IntegerField("Lenght", help_text="how wide is the item in cm", null=True)
    description = models.CharField("Description", max_length=400, null=True)
    price = models.IntegerField("Price", help_text="price in euro", null=True)
    smith_id = models.ForeignKey("Smiths", max_length=50, on_delete=models.SET_NULL, null=True, help_text="who made the item")
    image = models.ImageField("main image", upload_to="img", null=True)

    def __str__(self):
        return f" name:{ self.name } {self.price} "

class ProductImages(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE, null=True)
    images = models.FileField(upload_to='img', null=True)

class Landing_photos(models.Model):
    image = models.ImageField("first", upload_to="img", null=True)
    image = models.ImageField("second", upload_to="img", null=True)
    image = models.ImageField("third", upload_to="img", null=True)

class GaleryItem(models.Model):
    name = models.CharField("Names", max_length=200, null=True)
    image = models.ImageField("main foto", upload_to="img", null=True)

    def __str__(self):
        return f" name:{ self.name }   "


class GaleryImages(models.Model):
    galeryitem = models.ForeignKey(GaleryItem, default=None, on_delete=models.CASCADE, null=True)
    images = models.FileField(upload_to='img', null=True)
    

class product_Type(models.Model):
    type = models.CharField('Type', max_length=50,help_text='type', null=True)

    def __str__(self):
        return f" { self.type }"


class Smiths(models.Model):
    smith = models.CharField('Smith', max_length=50,help_text='smith who made the item', null=True)
    mobile_number = models.CharField("Mobile number", max_length=12, null=True)

    def __str__(self):
        return f"{ self.smith }"


class Comment(models.Model):
    name = models.CharField(max_length=50, null=True)
    body = models.TextField( null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


