from django.db import models

class Laptop(models.Model):
    Ram = models.IntegerField()
    Weight = models.FloatField()
    TouchScreen = models.BooleanField()
    Ips = models.BooleanField()
    Ppi = models.FloatField()
    HDD = models.IntegerField()
    SSD = models.IntegerField()
    Company = models.CharField(max_length=100)
    TypeName = models.CharField(max_length=100)
    Cpu_brand = models.CharField(max_length=100)
    Gpu_brand = models.CharField(max_length=100)
    Os = models.CharField(max_length=100)
