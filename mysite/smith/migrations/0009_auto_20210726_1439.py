# Generated by Django 3.2 on 2021-07-26 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smith', '0008_auto_20210726_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='galeryitem',
            name='name_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Name_en'),
        ),
        migrations.AlterField(
            model_name='galeryitem',
            name='name',
            field=models.CharField(max_length=200, null=True, verbose_name='Pavadinimas'),
        ),
    ]