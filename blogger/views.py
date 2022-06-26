from django.shortcuts import render
from blogger.forms import UserForm
from django.shortcuts import redirect

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserForm()


    return render(request, 'create_user.html', {'form': form})
