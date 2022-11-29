from django.db import models
from django.core import validators
from django.urls import reverse
from django.core.exceptions import ValidationError


class Service(models.Model):
    name = models.CharField('Название', max_length=100)
    content = models.TextField('Описание', blank=True)
    photo = models.ImageField('Фото', blank=True)
    price = models.FloatField('Цена', max_length=7)
    cat = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.PROTECT)
    slug = models.SlugField('URL', max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('service', kwargs={'service_slug': self.slug})

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['id']


class Category(models.Model):
    name = models.CharField('Категория', max_length=50)
    slug = models.SlugField('URL', max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'