from django.shortcuts import render, redirect
from .forms import UserLoginForm,UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User


def user_login(request):
    return render(request, 'accounts/login.html')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, email=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'You are login', 'success')
                return redirect('shop:home')
            else:
                messages.error(
                    request, 'username or password is not wrong', 'danger')
                return redirect('shop:home')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'you logged out successfully', 'success')
    return redirect('shop:home')

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['email'],cd['full_name'],cd['password'])
            user.save()
            messages.success(request, 'You Are Register Successfully', 'success')
            return redirect('shop:home')
    else:
        form = UserRegistrationForm()
    return render(request,'accounts/register.html',{'form':form})
