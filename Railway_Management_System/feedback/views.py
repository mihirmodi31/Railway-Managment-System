from django.shortcuts import render
from .models import Feedback

# Create your views here.

def feedback(request):
    e = request.GET['email']
    f = request.GET['feedback']
    n = request.GET['names']

    fd = Feedback.objects.all()
    ob = Feedback(name = n, email = e, feedbacks = f)
    ob.save()
    return render(request, "feed.html")