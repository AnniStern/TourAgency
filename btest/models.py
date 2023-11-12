from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=255)

class Resort(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

class Hotel(models.Model):
    resort = models.ForeignKey(Resort, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    distance_from_airport = models.IntegerField()
    star_rating = models.IntegerField()
    beach_info = models.TextField()

class Tourist(models.Model):
    name = models.CharField(max_length=255)

class Tour(models.Model):
    departure_date = models.DateField()
    return_date = models.DateField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.CharField(max_length=255)
    tourist = models.ForeignKey(Tourist, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
