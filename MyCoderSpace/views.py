from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from MyCoderSpace.models import *

class BlogList(ListView):
    model = BlogModel
    template_name = "blog.html"

class BlogDetail(DetailView):
    model = BlogModel
    template_name = "blog_detail.html"

class BlogCreate(LoginRequiredMixin, CreateView):
    model = BlogModel
    template_name = "createblog.html"
    success_url = reverse_lazy("home")
    fields = ['titulo', 'sub_titulo', 'cuerpo']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class BlogUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = BlogModel
    template_name = "blog_update.html"
    success_url = reverse_lazy("home")
    fields = ['titulo', 'sub_titulo', 'cuerpo']

    def test_func(self):
        exist = BlogModel.objects.filter(autor=self.request.user.id, id=self.kwargs['pk'])
        return True if exist else False

class BlogDelete(LoginRequiredMixin,UserPassesTestMixin, DeleteView):

    model = BlogModel
    template_name = "blog_delete.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        exist = BlogModel.objects.filter(autor=self.request.user.id, id=self.kwargs['pk'])
        return True if exist else False

class BlogLogin(LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy("home")


class BlogLogout(LogoutView):
    template_name = 'logout.html'





