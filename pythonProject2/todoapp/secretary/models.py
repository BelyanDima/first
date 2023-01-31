from datetime import date

from django.db import models
from django.urls import reverse


# Create your models here.

class ToDo(models.Model):
    title = models.CharField('Задача', max_length=500)
    created_at = models.DateTimeField('Выдана', auto_now=True)
    executor = models.ForeignKey('Executor', on_delete=models.PROTECT, verbose_name='Исполнитель')
    period_of_execution = models.DateField('Срок(дата) исполнения')
    is_complete = models.BooleanField('Исполнено', default=False)




    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['period_of_execution']

    def __str__(self):
        return self.title



class Executor(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name='Исполнитель')

    def get_absolute_url(self):
        return reverse('executor', kwargs={'executor_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'
        ordering = ['title']
