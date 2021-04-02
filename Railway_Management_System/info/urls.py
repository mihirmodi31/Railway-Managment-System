from django.urls import path, include
from . import views

urlpatterns = [
    path('info/', views.info, name = "info"),
    path('info/aboutus/', views.ab, name = "info/aboutus"),
    path('info/project/', views.pr, name = "info/project/"),
    path('info/feedback/', views.fb, name = "info/feedback/"),
]