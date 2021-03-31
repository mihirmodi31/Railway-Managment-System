from django.urls import path, include
from . import views

urlpatterns = [
    path('display/', views.display, name = "display")
]