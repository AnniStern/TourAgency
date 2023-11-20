from django.contrib import admin
from .models import Country, Resort, Hotel, Tourist, Tour

class ResortAdmin(admin.ModelAdmin):
    list_display = ('name', 'country_name')  # Отображаем название курорта и страны

    def country_name(self, obj):
        return obj.country.name  # Используем строковое представление страны

    country_name.short_description = 'Страна'  # Задаем "человеческую" подпись для отображения в админке

class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'resort_name', 'distance_from_airport', 'star_rating', 'beach_info')

    def resort_name(self, obj):
        return obj.resort.name  # Используем строковое представление курорта

    resort_name.short_description = 'Курорт'

class TourAdmin(admin.ModelAdmin):
    list_display = ('departure_date', 'return_date', 'hotel_name', 'room_type', 'tourist_name', 'price')

    def hotel_name(self, obj):
        return obj.hotel.name  # Используем строковое представление отеля

    def tourist_name(self, obj):
        return obj.tourist.name  # Используем строковое представление туриста

admin.site.register(Country)
admin.site.register(Resort, ResortAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Tourist)
admin.site.register(Tour, TourAdmin)
