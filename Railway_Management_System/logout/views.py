from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout as ulogout


def logout(request):
    ulogout(request)
    return redirect('../')