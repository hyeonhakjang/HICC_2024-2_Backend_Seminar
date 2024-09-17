from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

def register(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
                email=request.POST['email'], )
            auth.login(request, user)
            return redirect('accounts:login')
        return render(request, 'accounts/register.html')
    return render(request, 'accounts/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('hiccproject:home')
        else:
            return render(request, 'accounts/login_view.html')
    return render(request, 'accounts/login_view.html')

def logout_view(request):
    auth.logout(request)
    return redirect('hiccproject:home')