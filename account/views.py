from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from account.forms import LoginForm, RegisterForm, UpdateForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect("chat:home")

    if request.method == "POST":
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                messages.success(request, 'Logged in Successfully')
                login(request, user)
                return redirect("chat:home")
        else:
            return render(request, "account/login.html", {'form' : form})
    else:
        form = LoginForm()

    return render(request, "account/login.html", {'form' : form})


def register_view(request):
    if request.user.is_authenticated:
        return redirect("chat:home")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, "Registered Successfully")
            user = form.save()
        else:
            return render(request, "account/register.html", {'form' : form})
    else:
        form = RegisterForm()

    return render(request, "account/register.html", {'form' : form})


def logout_view(request):
    logout(request)
    return redirect("login")


def update_view(request, id):
    context = {}

    if request.method == 'POST':
        user = User.objects.get(id=id)
        form = UpdateForm(request.POST, instance=user)
        if form.is_valid():
            messages.success(request, "Profile Updated Successfully.")
            form.save()
            return redirect("chat:home")
    else:
        user = User.objects.get(id=id)
        form = UpdateForm(instance=user)

    context['form'] = form
    return render(request, 'account/update.html', context)       