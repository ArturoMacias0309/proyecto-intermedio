from django.db import models

# Create your models here.

class Donareg(models.Model):
    sabor=models.CharField(max_length=30)
    precio=models.IntegerField()

class Donaprem(models.Model):
    sabor= models.CharField(max_length=30)
    precio=models.IntegerField()

class Malteadas(models.Model):
    sabor= models.CharField(max_length=20)
    precio=models.IntegerField()
        





