from django.shortcuts import render
from .models import *
from itertools import groupby

def tour_list(request):
    tours = Tour.objects.all()
    return render(request, 'orders/tour_list.html', {'tours': tours})

def resort_list(request):
    hotels = Hotel.objects.all().order_by('resort__name', 'name')

    grouped_hotels = []
    for key, group in groupby(hotels, key=lambda x: x.resort.name):
        grouped_hotels.append((key, list(group)))

    return render(request, 'orders/resort_list.html', {'hotels': grouped_hotels})


def home(request):
    return render(request, 'orders/home.html')


