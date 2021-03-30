from django.shortcuts import render

# Create your views here.

def search(request):
    if request.method == "POST":
        trains = request.POST['trains']
        date = request.POST['date']
        seats = request.POST['seats']
        return render(request, "payment.html")
    
    else
        return render(request, "search.html")
