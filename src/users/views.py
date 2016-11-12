from django.shortcuts import render, redirect
from users.forms import *
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'users/index.html')


def reg(request):
    if request.POST:
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(request.POST.get('password'))
            user.save()
            return redirect('user')
        else:
            print form.errors
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})


def login_user(request):
    if request.POST:
        form = LoginForm(request.POST or None)

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'users/login.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('home')


