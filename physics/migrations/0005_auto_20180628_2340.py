# Generated by Django 2.0.6 on 2018-06-28 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('physics', '0004_auto_20180628_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='type',
            field=models.IntegerField(choices=[(1, 'З однією правильною відповіддю'), (2, 'Встановлення відповідності'), (3, 'З відкритою відповіддю')], default='1', verbose_name='Тип завдання'),
        ),
    ]
