# Generated by Django 2.2 on 2022-07-21 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recycle', '0055_auto_20220720_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_slug',
            field=models.CharField(default='article2022-07-21 18:35:02.657723', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_slug',
            field=models.CharField(default='slug2022-07-21 18:35:02.532953', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_slug',
            field=models.CharField(default='product2022-07-21 18:35:02.655912', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='region',
            name='region_slug',
            field=models.CharField(default='region2022-07-21 18:35:02.659017', max_length=200, verbose_name='URL'),
        ),
    ]
