from django.urls import path, include
from . import views

urlpatterns = [
    path('info/', views.info, name = "info")
]