# Generated by Django 3.2 on 2021-07-26 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smith', '0006_auto_20210726_1406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.AddField(
            model_name='product',
            name='name_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Item name en'),
        ),
    ]