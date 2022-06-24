from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from blogger.models import Avatar
from django.contrib.auth.decorators import login_required

class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'create_user.html'
    success_url = reverse_lazy('home')
    form_class = UserCreationForm
    success_message = '¡Perfil creado satisfactoriamente!'

class BloggerProfile(DetailView):
    model = User
    template_name = "profile.html"

class BloggerUpdate(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "update_profile.html"
    fields = ["username", "email", "first_name", "last_name"]
    success_message = '¡Perfil actualizado satisfactoriamente!'
    
    def get_success_url(self):
      return reverse_lazy("profile", kwargs={"pk": self.request.user.id})
