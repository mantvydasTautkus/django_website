# Generated by Django 3.2 on 2021-07-26 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smith', '0005_rename_galeryitem_galeryimages_galeryitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name_lt',
            field=models.CharField(max_length=200, null=True, verbose_name='Item name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200, null=True, verbose_name='Item name'),
        ),
    ]
