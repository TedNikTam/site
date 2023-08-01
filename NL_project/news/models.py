from datetime import datetime
from django.db import models

class Articles(models.Model):
    title = models.CharField('Название', max_length=100, default='Статья без названия')
    anons = models.CharField('Анонс', max_length=350)
    full_text = models.TextField('Статья')
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title
    
    class Meta: # множественное и единственно число названия таблицы
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
