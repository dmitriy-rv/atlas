### -*- coding: utf-8 -*- ###

from __future__ import unicode_literals

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from image_cropping import ImageRatioField

# Create your models here.

class Article(models.Model):
	title = models.CharField(max_length=30, verbose_name='Заголовок')
	text = RichTextUploadingField(verbose_name='Содержание')

	def __unicode__(self):
		return self.title

class Excursions(models.Model):
	title = models.CharField(max_length=30, verbose_name='Заголовок')
	main_text = models.CharField(max_length=160, verbose_name='Анонс для списка')
	text = RichTextUploadingField(verbose_name='Содержание')
	list_image = models.ImageField(upload_to='./img', verbose_name='Изображение в список')
	cropping = ImageRatioField('list_image', '500x300', allow_fullsize=True)
	main = models.BooleanField(default=False, blank=True,  verbose_name='На главную')
	slide_image = models.ImageField(upload_to='./img', blank=True, verbose_name='Изображение на главную')
	slide_cropping = ImageRatioField('slide_image', '650x430', allow_fullsize=True)
	slide = models.BooleanField(default=False, blank=True,  verbose_name='Добавить фотоальбом') 

	def __unicode__(self):
		return self.title

class Image(models.Model):
	title = models.ForeignKey(Excursions)
	images = models.ImageField(upload_to='./img', verbose_name='Фотографии')

class Gallery(models.Model):
	title = models.CharField(max_length=30, verbose_name='Название')
	image = models.ImageField(upload_to='./img', blank=True, verbose_name='Изображение')
	cropping = ImageRatioField('image', '380x240', allow_fullsize=True)
	
	def __unicode__(self):
		return self.title


class Map(models.Model):
	title = models.CharField(max_length=30, verbose_name='Название')
	map = models.CharField(max_length=90, blank=True)

	def __unicode__(self):
		return self.title