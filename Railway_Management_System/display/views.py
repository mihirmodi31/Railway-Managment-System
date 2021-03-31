from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def display(request):
    source = request.GET['src']
    destination = request.GET['dst']
    date = request.GET['dates']

    return render(request, "display.html", {'src': source, 'dst': destination, 'date': date})
