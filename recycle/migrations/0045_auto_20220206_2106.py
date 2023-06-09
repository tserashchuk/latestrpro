# Generated by Django 3.0 on 2022-02-06 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recycle', '0044_auto_20220206_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_slug',
            field=models.CharField(default='article2022-02-06 21:06:40.332522', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_slug',
            field=models.CharField(default='slug2022-02-06 21:06:40.301121', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='region',
            name='region_slug',
            field=models.CharField(default='region2022-02-06 21:06:40.333307', max_length=200, verbose_name='URL'),
        ),
    ]
