from django.db import models

from flower import settings




class TextItem(models.Model):
    job = models.TextField(verbose_name='Наши услуги')
    mission = models.TextField(verbose_name='Почему мы')
    company = models.TextField(verbose_name='О компании')