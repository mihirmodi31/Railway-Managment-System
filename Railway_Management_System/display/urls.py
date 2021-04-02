from django.urls import path, include
from . import views

urlpatterns = [
    path('display/', views.display, name = "display"),
    path('inter/', views.inter, name = "inter"),
    path('inter/aboutus/', views.ab, name = "inter/aboutus"),
    path('inter/project/', views.pr, name = "inter/project/"),
    path('inter/feedback/', views.fb, name = "inter/feedback/"),
    path('display/aboutus/', views.ab1, name = "display/aboutus1"),
    path('display/project/', views.pr1, name = "display/project/"),
    path('display/feedback/', views.fb1, name = "display/feedback/"),
]