from django.shortcuts import render
from .models import *

def tour_list(request):
    tours = Tour.objects.all()
    return render(request, 'orders/tour_list.html', {'tours': tours})

def resort_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'orders/resort_list.html', {'hotels': hotels})

def home(request):
    return render(request, 'orders/home.html')