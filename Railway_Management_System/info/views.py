from django.db.models.fields import IntegerField
from django.shortcuts import render
from django.http import HttpResponse
from .models import Avail, Tickets
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
        avails = Avail.objects.all()
        isavail = "no"

        train1 = {}
        for train in trains:
            if int(train.pricesl) == int(price) or int(train.price2s) == int(price):
                train1 = train
                break
        
        s1 = 0
        s2 = 0

        for x in avails:
            if int(x.pnr) == int(train.pnr):
                if int(x.seat) < int(num):
                    isavail = "no"
                else:
                    isavail = "yes"
                    s1 = int(x.seat)
                    s2 = int(x.seat) - int(num) + int(1)
                    x.seat = int(x.seat) - int(num)
                    # t = Tickets(date = dates, no = num, total_price = tprice, passangers = q, ages = age)
                    # t.save()            
        
        return render(request, "info.html", {'train1' : train1, 'age' : age, 'price' : price, 'no' : num, 'q' : q, 'dates' : dates, 'tprice' : tprice, 'isavail' : isavail, 's1' : s1, 's2' : s2})