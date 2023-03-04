from django.db import models

# Create your models here.

class Info(models.Model):
    id = models.IntegerField(primary_key=True)
    med = models.CharField(max_length=70)
    name = models.CharField(max_length=70)
    start = models.CharField(max_length=70)
    end = models.CharField(max_length=70)
    stations = models.IntegerField()
    seat_no = models.IntegerField()

class Station(models.Model):
    transport_id = models.ForeignKey(Info, on_delete=models.CASCADE)
    arr_station = models.CharField(max_length=70)
    arr_time = models.TimeField()
    arr_date = models.DateField()
    dep_station = models.CharField(max_length=70)
    dep_time = models.TimeField()
    dep_date = models.DateField()
    seats = models.IntegerField()

class Passenger(models.Model):
    passenger_id = models.AutoField()
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    train_id = models.ForeignKey(Info,on_delete=models.CASCADE)
    starting_station = models.CharField(max_length=20)
    ending_station = models.CharField(max_length=20)
    starting_time = models.TimeField()
    ending_time = models.TimeField()
    starting_date = models.DateField()
    ending_date = models.DateField()