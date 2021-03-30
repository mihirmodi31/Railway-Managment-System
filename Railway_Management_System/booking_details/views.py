from django.shortcuts import render

# Create your views here.

def booking_details(request):
    return render(request, "booking_details.html")