from django.contrib import messages
from django.shortcuts import redirect, render
from info.models import Avail

# Create your views here.

def seat(request):
    avails = Avail.objects.all()
    status = "no"

    pswd = request.GET['adpas']
    if pswd == "Admin.123":
        status = "yes"
        for x in avails:
            x.seatsl = 50
            x.seat2s = 50
            x.save()

    
    return render(request, "seat.html", {'status' : status})