from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Game(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=False)
    genre = models.TextField()
    description = models.TextField()
    review = models.IntegerField()
    price = models.FloatField()

class Producer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=False)
    description = models.TextField()

class Comand (models.Model):
    id = models.AutoField(primary_key=True)
    game = models.ForeignKey(Game, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    price = models.FloatField()

