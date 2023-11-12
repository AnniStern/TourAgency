from django.contrib import admin
from .models import Country, Resort, Hotel, Tourist, Tour

admin.site.register(Country)
admin.site.register(Resort)
admin.site.register(Hotel)
admin.site.register(Tourist)
admin.site.register(Tour)