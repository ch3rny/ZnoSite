from django.db import models
import datetime
from storages.backends.ftp import FTPStorage
from django.contrib.auth.models import User
from django.utils import timezone


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
    correct_answer = models.CharField(max_length=12, verbose_name="Правильна відповідь")

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


class Bundle(models.Model):
    name = models.CharField(max_length=75, verbose_name='Підбірка')
    cover = models.ImageField(upload_to='bundles', default='bundles/bundle.jpg', verbose_name="Обкладинка", storage=fs)
    tasks = models.ManyToManyField(Task, verbose_name="Завдання", blank=True)
    shared = models.ManyToManyField(User, verbose_name="Доступно для", blank=True)
    author_id = models.IntegerField(verbose_name='Автор', default='3')
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Дата створення")
    edited_date = models.DateTimeField(default=timezone.now, verbose_name="Останні зміни")

    class Meta:
        verbose_name = 'Підбірка'
        verbose_name_plural = 'Підбірки'

    def __str__(self):
        return self.name


class TestAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Користувач')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name='Завдання')
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, verbose_name='Тема')
    user_answer = models.CharField(max_length=12, blank=True, verbose_name='Відповідь користувача')
    is_true = models.BooleanField(verbose_name='Правильна відповідь')
    date = models.DateTimeField(default=timezone.now, verbose_name='Дата відповіді')

    class Meta:
        verbose_name_plural = "Відповіді користувачів"

    def __str__(self):
        return str(self.task.id)+'-'+str(self.user)+'('+str(self.date)+')'
