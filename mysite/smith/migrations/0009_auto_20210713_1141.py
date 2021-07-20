# Generated by Django 3.2 on 2021-07-13 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smith', '0008_auto_20210713_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galeryitem',
            name='image',
            field=models.ImageField(null=True, upload_to='img', verbose_name='main foto'),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='images',
            field=models.FileField(upload_to='img'),
        ),
        migrations.CreateModel(
            name='GaleryImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='img')),
                ('GaleryItem', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='smith.galeryitem')),
            ],
        ),
    ]