from django.urls import path, include
from . import views

urlpatterns = [
    path('booking_details/', views.booking_details, name = "booking_details"),
]