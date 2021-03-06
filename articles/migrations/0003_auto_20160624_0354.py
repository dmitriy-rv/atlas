# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-24 00:54
from __future__ import unicode_literals

from django.db import migrations, models
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20160624_0334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery_image',
            name='title',
        ),
        migrations.AddField(
            model_name='gallery',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '380x240', adapt_rotation=False, allow_fullsize=True, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='image',
            field=models.ImageField(blank=True, upload_to='./img', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='title',
            field=models.CharField(max_length=30, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
        migrations.DeleteModel(
            name='Gallery_Image',
        ),
    ]
