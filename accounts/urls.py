from django.urls import path
from . import views            #from base import views


urlpatterns = [
    path('', views.home),   #dodajemy tutaj takie nazwy jak w pliku views nazywaly sie funkcje
    path('products/', views.products),
    path('customer/', views.customer), 
]