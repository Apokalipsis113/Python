from django.db import models
from django.utils import timezone


class Genge(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    genre = models.ForeignKey(Genge, on_delete=models.CASCADE)
    date_created = models.DateField(default=timezone.now)
