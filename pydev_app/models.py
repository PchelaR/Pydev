from django.db import models
from tinymce.models import HTMLField
from slugify import slugify


class Category(models.Model):

    class Meta:
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"

    CATEGORY_CHOICES = [
        ('backend', 'Backend'),
        ('frontend', 'Frontend'),
    ]
    name = models.CharField(max_length=50, choices=CATEGORY_CHOICES, unique=True)
    description = models.TextField(blank=False)
    slug = models.SlugField(editable=False, unique=True, max_length=255)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.get_name_display()


class Topic(models.Model):

    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='topics')
    slug = models.SlugField(editable=False, max_length=255)

    class Meta:
        unique_together = ('slug', 'category')

        verbose_name = "Тему"
        verbose_name_plural = "Темы"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Module(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=False)
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE, related_name='modules')
    slug = models.SlugField(editable=False, max_length=255)

    class Meta:
        unique_together = ('slug', 'topic')

        verbose_name = "Модуль"
        verbose_name_plural = "Модули"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = HTMLField()
    module = models.ForeignKey('Module', on_delete=models.CASCADE, related_name='lessons')
    slug = models.SlugField(editable=False, max_length=255)

    class Meta:
        unique_together = ('slug', 'module')

        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Resource(models.Model):

    class Meta:
        verbose_name = "Ресурс"
        verbose_name_plural = "Ресурсы"

    CATEGORY_CHOICES = [
        ('playlist', 'Плейлисты'),
        ('website', 'Сайты'),
        ('book', 'Книги'),
        ('documentation', 'Документация'),
        ('course', 'Курсы'),
    ]

    title = models.CharField(max_length=255)
    url = models.URLField(max_length=2000)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='website')

    def __str__(self):
        return self.title
