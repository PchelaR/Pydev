# Generated by Django 5.1 on 2024-08-30 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pydev_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категорию', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'verbose_name': 'Урок', 'verbose_name_plural': 'Уроки'},
        ),
        migrations.AlterModelOptions(
            name='module',
            options={'verbose_name': 'Модуль', 'verbose_name_plural': 'Модули'},
        ),
        migrations.AlterModelOptions(
            name='resource',
            options={'verbose_name': 'Ресурс', 'verbose_name_plural': 'Ресурсы'},
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'verbose_name': 'Тему', 'verbose_name_plural': 'Темы'},
        ),
    ]
