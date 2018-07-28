from django.db import models
import datetime
from storages.backends.ftp import FTPStorage
fs = FTPStorage()


class Task (models.Model):
    YEAR_CHOICES = []
    for r in range(2007, datetime.datetime.now().year+1):
        YEAR_CHOICES.append((r, r))
    NUMBER_CHOICES = []
    for r in range(1, 39):
        NUMBER_CHOICES.append((r, r))
    TYPE_CHOICES = (
        (1, 'З однією правильною відповіддю'),
        (2, 'Встановлення відповідності'),
        (3, 'З відкритою відповіддю')
    )
    ZNO_CHOICES = (
        (1, 'Основне'),
        (2, 'Пробне'),
        (3, 'Додаткова сесія')
    )

    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year, verbose_name='Рік')
    number = models.IntegerField(choices=NUMBER_CHOICES, default='1', verbose_name='Номер завдання')
    zno_type = models.IntegerField(choices=ZNO_CHOICES, default='1',verbose_name="Тип ЗНО")
    theme = models.ForeignKey('Theme', on_delete=models.CASCADE, verbose_name="Розділ")
    type = models.IntegerField(choices=TYPE_CHOICES, default='1', verbose_name="Тип завдання")
    task_image = models.ImageField(upload_to='uploads', null=False, blank=False, verbose_name="Завдання", storage=fs)
    correct_answer = models.CharField(max_length=12,verbose_name="Правильна відповідь")

    class Meta:
        verbose_name = 'Завдання'
        verbose_name_plural = 'Завдання'

    def __str__(self):
        p = '.'
        if self.zno_type == 2:
            p = '(п).'
        if self.zno_type == 3:
            p = '(д).'
        return str(self.year)+p+str(self.number)


class Theme(models.Model):
    name = models.CharField(max_length=200, verbose_name='Тема')

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Теми'
    def __str__(self):
        return self.name
