from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import CustomUserCreationForm, LoginForm


class UserRegisterView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'users_app/register.html'
    success_url = reverse_lazy('users:register_success')



class UserLoginView(LoginView):
    template_name = 'users_app/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('homepage')


class SuccessView(TemplateView):
    template_name = 'users_app/success_register.html'