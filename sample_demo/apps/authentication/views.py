from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("dashboard")
    else:
        login_form = LoginForm()
    return render(request, "login/login.html", {"form": login_form})

def register(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        try:
            User.objects.get(username=request.POST["username"])
        except User.DoesNotExist:
            register_form.save()
            return redirect("login")
    else:
        register_form = RegisterForm()
    return render(request, "register/register.html", {"form": register_form})

def logout(request):
    if request.method == "POST":
        auth_logout(request)
    return redirect("login")