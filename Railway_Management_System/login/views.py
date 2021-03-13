from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login as ulogin
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, "index.html")

def login(request):
    if request.method == "POST":
        usernames = request.POST['uname']
        passwords = request.POST['pswd']

        user = authenticate(username = usernames, password = passwords)
        if user is not None:
            ulogin(request, user)
            messages.success(request, usernames)
            return redirect("../")
        else:
            messages.error(request, "Invalide Credential")
            return render(request, "login.html")
    else:
        return render(request, "login.html")

    