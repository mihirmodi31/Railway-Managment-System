from django.db.models.fields import IntegerField
from django.shortcuts import render
from django.http import HttpResponse
from .models import Tickets
from display.models import Trains

# Create your views here.

def info(request):
    if request.method == "GET":
        age = request.GET['age']
        q = request.GET['q']
        price = (request.GET['type'])
        num = request.GET['no']
        dates = request.GET['dates']

        tprice = (int(num) * int(price))
        trains = Trains.objects.all()

        train1 = {}
        for train in trains:
            if int(train.pricesl) == int(price) or int(train.price2s) == int(price):
                train1 = train
                break

        # t = Tickets(date = dates, no = num, total_price = tprice, passangers = q, ages = age)
        # t.save()
        
        return render(request, "info.html", {'train1' : train1, 'age' : age, 'price' : price, 'no' : num, 'q' : q, 'dates' : dates, 'tprice' : tprice})