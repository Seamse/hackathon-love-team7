from django.shortcuts import render, redirect
from django.contrib.auth import logout
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def landing(request):
    """ docstring """
    return render(request, 'home/landing.html')
      

def sign_up(request):
    """ docstring """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'home/sign-up.html', {'form': form})

@login_required
def logout_view(request):
    """ docstring """
    logout(request)
    return redirect('landing-home')

