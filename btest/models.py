# models.py

from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название страны')

    def __str__(self):
        return self.name

class Resort(models.Model):
    country = models.ForeignKey(Country, on_delete=models.PROTECT, verbose_name='Страна')
    name = models.CharField(max_length=255, verbose_name='Название курорта')

    def __str__(self):
        return self.name

class Hotel(models.Model):
    resort = models.ForeignKey(Resort, on_delete=models.PROTECT, verbose_name='Курорт')
    name = models.CharField(max_length=255, verbose_name='Название отеля')
    distance_from_airport = models.IntegerField(verbose_name='Расстояние от аэропорта (км)')
    star_rating = models.IntegerField(verbose_name='Количество звёзд')
    beach_info = models.TextField(verbose_name='Информация о пляже')

    def __str__(self):
        return self.name

class Tourist(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя туриста')

    def __str__(self):
        return self.name

class Tour(models.Model):
    departure_date = models.DateField(verbose_name='Дата отправления')
    return_date = models.DateField(verbose_name='Дата возвращения')
    hotel = models.ForeignKey(Hotel, on_delete=models.PROTECT, verbose_name='Отель')
    room_type = models.CharField(max_length=255, verbose_name='Тип номера')
    tourist = models.ForeignKey(Tourist, on_delete=models.PROTECT, verbose_name='Турист')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return f'{self.hotel} - {self.tourist} - {self.departure_date}'
