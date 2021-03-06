from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, "index.html")

def login(request):
    if request.method == "POST":
        username = request.POST['uname']
        password = request.POST['pswd']

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return render(request, "hello.html")
        else:
            messages.error(request, "Invalide Credential")
            return render(request, "login.html")
    else:
        return render(request, "login.html")

    