from django.shortcuts import render
from django.contrib.auth.models import User
from auth.forms import CreateUsersForm, LoginUseForm
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(
        request,
        'home.html'
    )


def signup(request):
    form = CreateUsersForm
    if request.method == 'POST':
        form = CreateUsersForm(request.POST)
        if form.is_valid():
            login = request.POST.get("login")
            password = request.POST.get("password")
            conf_password = request.POST.get("conf_password")
            if password == conf_password:
                user = User.objects.create_user(username=login, password=password)
                user.save()
                return render(
                    request,
                    'home.html')
    context = {
        'form': form
    }
    return render(
        request,
        'signup.html',
        context,
    )

def logout_user(request):
    logout(request)
    return render(request, "logout.html")


def login_user(request):
    form = LoginUseForm
    if request.method == 'POST':
        form = LoginUseForm(request.POST)
        if form.is_valid():
            name = request.POST.get("login")
            password = request.POST.get("password")
            user = authenticate(username=name, password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return render(
                        request,
                        'home.html'
                    )

    context = {
        'form':form
    }
    return render(
        request,
        'login.html',
        context,
    )
