from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from users.forms import UserLoginForm

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Login',
        'form': form,
    }
    return render(request, 'users/login.html', context)


def registration(request):
    context = {
        "title": "Регистрация"
    }
    return render(request, 'users/registration.html', context)

def profile(request):
    context = {
        "title": "Мой профиль"
    }
    return render(request, 'users/profile.html', context)

def logout(request):
    context = {}
    return render(request, '', context)
