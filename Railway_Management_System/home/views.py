from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def aboutus(request):
    return render(request, "aboutus.html")

def project(request):
    return render(request, "project.html")

def feedback(request):
    return render(request, "feedback.html")

