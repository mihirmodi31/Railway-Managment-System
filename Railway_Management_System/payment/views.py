from django.shortcuts import render

# Create your views here.

def payment(request):
    if request.method == "POST":
        bank = request.POST['bank']
        acc = request.POST['acc']
        ifsc = request.POST['ifsc']
        
    return render(request, "payment.html")