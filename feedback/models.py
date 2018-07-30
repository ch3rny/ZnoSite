from django.db import models
from django.utils import timezone
from storages.backends.ftp import FTPStorage
fs = FTPStorage()


class Review(models.Model):
    author = models.CharField(max_length=75, blank=False, verbose_name='Ім`я')
    mail = models.EmailField(verbose_name='E-mail', default='', blank=True)
    text = models.TextField(verbose_name='Повідомлення')
    created_time = models.DateTimeField(default=timezone.now)
    attachment = models.FileField(upload_to='attachments', default=None, blank=True, verbose_name='Вкладення', storage=fs)
    unread = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Відгук'
        verbose_name_plural = 'Відгуки'

    def __str__(self):
        return self.created_time
