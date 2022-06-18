from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from MyCoderSpace.models import *
from MyCoderSpace.forms import *
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import loader
from django.views import View
from MyCoderSpace.forms import CrearBlog

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

class CrearBlog(View):
    form_class = CrearBlog
    context = {
        "title": "Submit Url",
        "formulario": form_class
    }
    template_name = 'blog.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"formulario": context})

    def post(self, request, *args, **kwargs):
        formulario = self.form_class(request.POST)
        if formulario.is_valid():
            print(formulario.cleaned_data)
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {"formulario": formulario})




