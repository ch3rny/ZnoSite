# Generated by Django 2.0.6 on 2018-12-22 22:07

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('physics', '0012_answer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Answer',
            new_name='TestAnswer',
        ),
    ]
