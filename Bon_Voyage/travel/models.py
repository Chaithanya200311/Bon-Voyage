from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Transport(models.Model):
    id = models.IntegerField(primary_key=True)
    mode = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    start = models.CharField(max_length=50)
    end = models.CharField(max_length=50)
    start_date = models.DateField(default=datetime.now())
    end_date = models.DateField(default=datetime.now())
    start_time = models.TimeField(default=datetime.now())
    end_time = models.TimeField(default=datetime.now())
    no_seats = models.IntegerField()
    total_time = models.TimeField()

class Passenger(models.Model):
    id = models.AutoField(primary_key=True)
    User_id = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    train_id = models.ForeignKey(Transport,on_delete=models.CASCADE)