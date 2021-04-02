from django.urls import path, include
from . import views

urlpatterns = [
    path('display/', views.display, name = "display"),
    path('inter/', views.inter, name = "inter"),
]