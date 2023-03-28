# Generated by Django 2.2 on 2022-03-09 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recycle', '0053_auto_20220209_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_slug',
            field=models.CharField(default='article2022-03-09 16:40:15.483949', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_slug',
            field=models.CharField(default='slug2022-03-09 16:40:15.395236', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_slug',
            field=models.CharField(default='product2022-03-09 16:40:15.483102', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='region',
            name='region_slug',
            field=models.CharField(default='region2022-03-09 16:40:15.484708', max_length=200, verbose_name='URL'),
        ),
    ]
