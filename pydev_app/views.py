from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import TemplateView, DetailView, ListView
from .models import Category, Topic, Module, Lesson, Resource


class HomepageView(LoginRequiredMixin, TemplateView):
    template_name = 'pydev_app/homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.prefetch_related('topics').all()
        context['categories'] = categories
        return context


class DatabaseOfQuestionsView(LoginRequiredMixin, TemplateView):
    template_name = 'pydev_app/database_of_questions.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.prefetch_related('topics').all()
        context['categories'] = categories
        return context


class DetailsCategoryView(LoginRequiredMixin, DetailView):
    model = Category
    template_name = 'pydev_app/detail_category.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.object
        topics = Topic.objects.filter(category=category)
        context['topics'] = topics
        return context


class DetailsTopicView(LoginRequiredMixin, DetailView):
    model = Topic
    template_name = 'pydev_app/detail_topic.html'
    context_object_name = 'topic'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        topic = self.get_object()
        modules = Module.objects.filter(topic=topic)
        lessons = Lesson.objects.filter(module__in=modules)
        context['modules'] = modules
        context['lessons'] = lessons
        return context


class DetailsLessonView(LoginRequiredMixin, DetailView):
    model = Lesson
    template_name = 'pydev_app/detail_lesson.html'
    context_object_name = 'lesson'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lesson = self.get_object()
        topic = lesson.module.topic
        context['back_url'] = reverse('detail_topic', kwargs={'slug': topic.slug})
        return context


class AdditionalResourceList(LoginRequiredMixin, ListView):
    model = Resource
    template_name = 'pydev_app/additional_resource.html'
    context_object_name = 'resources'

    def get_queryset(self):
        return Resource.objects.all().order_by('category', 'title')


class AboutUsView(LoginRequiredMixin, TemplateView):
    template_name = 'pydev_app/about_us.html'


class ApiEndpointsView(TemplateView):
    template_name = 'pydev_app/api_endpoints.html'