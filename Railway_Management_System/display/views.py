from display.models import Trains
from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def display(request):
    source = request.GET['src']
    destination = request.GET['dst']
    date = request.GET['dates']

    trains = Trains.objects.all()

    return render(request, "display.html", {'trains' : trains, 'src' : source, 'dst' : destination})
