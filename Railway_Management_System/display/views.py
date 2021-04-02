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

def inter(request):
    trains = Trains.objects.all()
    ids = request.GET['id']
    pricesl = request.GET['pricesl']
    price2s = request.GET['price2s']
    return render(request, "inter.html", {'trains' : trains, 'ids' : ids, 'pricesl' : pricesl, 'price2s' : price2s})