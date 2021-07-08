from django.db import models
from django.db.models.base import Model
from django.urls import reverse
import uuid


class Product(models.Model):
    name = models.CharField("Name", max_length=200)
    height = models.IntegerField("Height", help_text="how tall is the item in cm ")
    whith = models.IntegerField("Whith", help_text="how wide is the item in cm")
    lenght = models.IntegerField("Lenght", help_text="how wide is the item in cm")
    description = models.CharField("Description", max_length=400)
    city = models.CharField("City", max_length=200, help_text="city where item can be picked up")
    price = models.IntegerField("Price", help_text="price in euro")
    smith_id = models.ForeignKey("Smiths", max_length=50, on_delete=models.SET_NULL, null=True, help_text="who made the item")
    type_id = models.ForeignKey("ItemKind", max_length=50, on_delete=models.SET_NULL, null=True, help_text="type of the item")

    def __str__(self):
        return f" name:{ self.name }   _location:{self.city}  _price:{self.price}"

class Smiths(models.Model):
    smith = models.CharField('Smith', max_length=50,help_text='smith who made the item')

    def __str__(self):
        return f"{ self.smith }"

class ItemKind(models.Model):
    type = models.CharField("Type", max_length=50, help_text='type of the item ')

    def __str__(self):
        return f"{ self.type }"





# class Genre(models.Model):
#     name = models.CharField('Pavadinimas', max_length=200,help_text='Įveskite knygos žanrą (pvz. detektyvas)')

#     def __str__(self):
#         return f"{ self.name }"


# class Book(models.Model):
#     title = models.CharField('Pavadinimas', max_length=200)
#     author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
#     summary = models.TextField(
#         'Aprašymas', max_length=1000, help_text='Trumpas knygos aprašymas')
#     isbn = models.CharField(
#         'ISBN', max_length=13, help_text='13 Simbolių <a href="https://www.isbn-international.org/content/what-isbn">ISBN kodas</a>')
#     genre = models.ManyToManyField(
#         Genre, help_text='Išrinkite žanrą(us) šiai knygai')

#     def __str__(self):
#         return self.title

#     def get_absolute_url(self):
#         return reverse('book-detail', args=[str(self.id)])


# class BookInstance(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4,help_text='Unikalus ID knygos kopijai')
#     book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
#     due_back = models.DateField('Bus prieinama', null=True, blank=True)

#     LOAN_STATUS = (
#         ('a', 'Administruojama'),
#         ('p', 'Paimta'),
#         ('g', 'Galima paimti'),
#         ('r', 'Rezervuota'),
#     )

#     status = models.CharField(
#         max_length=1,
#         choices=LOAN_STATUS,
#         blank=True,
#         default='a',
#         help_text='Statusas',
#     )

#     class Meta:
#         ordering = ['due_back']

#     def __str__(self):
#         return f'{self.id} ({self.book.title})'


# class Author(models.Model):
#     """Model representing an author."""
#     first_name = models.CharField('Vardas', max_length=100)
#     last_name = models.CharField('Pavardė', max_length=100)

#     class Meta:
#         ordering = ['last_name', 'first_name']

#     def get_absolute_url(self):
#         return reverse('author-detail', args=[str(self.id)])

#     def __str__(self):
#         return f'{self.last_name} {self.first_name}'
