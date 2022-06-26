from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
from blogger.models import Avatar
>>>>>>> f6ca7e7598b410628912125949f7b288ba679a80
from django.contrib.auth.decorators import login_required
from blogger.forms import UserForm
from django.shortcuts import redirect

<<<<<<< HEAD
def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserForm()


    return render(request, 'create_user.html', {'form': form})

=======

=======

>>>>>>> refs/remotes/origin/main
class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'create_user.html'
    success_url = reverse_lazy('home')
    form_class = UserCreationForm
    success_message = '¡Perfil creado satisfactoriamente!'
=======
# """ class SignUpView(SuccessMessageMixin, CreateView):
#     template_name = 'create_user.html'
#     success_url = reverse_lazy('home')
#     form_class = UserCreationForm
#     success_message = '¡Perfil creado satisfactoriamente!' """
>>>>>>> f6ca7e7598b410628912125949f7b288ba679a80

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
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> refs/remotes/origin/main
=======
>>>>>>> refs/remotes/origin/main
=======

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserForm()


    return render(request, 'create_user.html', {'form': form})

>>>>>>> f6ca7e7598b410628912125949f7b288ba679a80
