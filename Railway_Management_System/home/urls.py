from django.urls import path, include
from . import views

urlpatterns = [
    path('aboutus', views.aboutus, name = "aboutus"),
    path('project', views.project, name = "project"),
    path('feedback', views.feedback, name = "feedback"),
]
