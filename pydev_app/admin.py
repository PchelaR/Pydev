from django.contrib import admin
from .models import Category, Topic, Module, Lesson, Resource


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'topic')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'module')

@admin.register(Resource)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title',)
