from django.urls import path, include
from . import views

urlpatterns = [
    path('feedback/', views.feedback, name = "feedback"),
]
