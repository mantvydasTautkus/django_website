from os import name
from django.core.paginator import EmptyPage
from django.db import models
from django.db.models.base import Model
from django.urls import reverse
import uuid


class Product(models.Model):
    name = models.CharField("Names", max_length=200)
    height = models.IntegerField("Height", help_text="how tall is the item in cm ")
    whith = models.IntegerField("Whith", help_text="how wide is the item in cm")
    lenght = models.IntegerField("Lenght", help_text="how wide is the item in cm")
    description = models.CharField("Description", max_length=400)
    city = models.CharField("City", max_length=200, help_text="city where item can be picked up")
    price = models.IntegerField("Price", help_text="price in euro")
    smith_id = models.ForeignKey("Smiths", max_length=50, on_delete=models.SET_NULL, null=True, help_text="who made the item")
    type_id = models.ForeignKey("ItemKind", max_length=50, on_delete=models.SET_NULL, null=True, help_text="type of the item")
    image = models.ImageField("main image", upload_to="img", null=True)

    def __str__(self):
        return f" name:{ self.name }   _location:{self.city}  _price:{self.price}"

class ProductImages(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='img')



class GaleryItem(models.Model):
    name = models.CharField("Names", max_length=200)
    description = models.CharField("Description", max_length=200)
    image = models.ImageField("main foto", upload_to="img", null=True)

    def __str__(self):
        return f" name:{ self.name }   description:{self.description} "


class GaleryImages(models.Model):
    GaleryItem = models.ForeignKey(GaleryItem, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='img')
    



class Smiths(models.Model):
    smith = models.CharField('Smith', max_length=50,help_text='smith who made the item')

    def __str__(self):
        return f"{ self.smith }"

class ItemKind(models.Model):
    type = models.CharField("Type", max_length=50, help_text='type of the item ')

    def __str__(self):
        return f"{ self.type }"


class Comment(models.Model):
    name = models.CharField(max_length=50)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"