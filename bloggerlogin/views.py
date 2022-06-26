from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from MyCoderSpace.models import *
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import loader
from django.views import View

class BlogLogin(LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy("home")


class BlogLogout(LogoutView):
    template_name = 'logout.html'
