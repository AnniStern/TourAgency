from django.urls import path
from .views import tour_list, resort_list
from .views import home
urlpatterns = [
    path('tours/', tour_list, name='tour_list'),
    path('resorts/', resort_list, name='resort_list'),
    path('', home, name='home'),
]

