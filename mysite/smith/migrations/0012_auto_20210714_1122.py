# Generated by Django 3.2 on 2021-07-14 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smith', '0011_auto_20210714_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galeryitem',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='img', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='galeryitem',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='img', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='galeryitem',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='img', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='galeryitem',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='img', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='galeryitem',
            name='image6',
            field=models.ImageField(blank=True, null=True, upload_to='img', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='galeryitem',
            name='image7',
            field=models.ImageField(blank=True, null=True, upload_to='img', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='galeryitem',
            name='image8',
            field=models.ImageField(blank=True, null=True, upload_to='img', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='img', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='img', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='img', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='img', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image6',
            field=models.ImageField(blank=True, null=True, upload_to='img', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image7',
            field=models.ImageField(blank=True, null=True, upload_to='img', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image8',
            field=models.ImageField(blank=True, null=True, upload_to='img', verbose_name='image'),
        ),
    ]
