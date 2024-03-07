from django.db import models


TYPES = (
    (1, 'Autos'),
    (2, 'Pickups y Comerciales'),
    (3, 'SUVs y Crossovers')
)

class Characteristic(models.Model):
    title = models.CharField(max_length=150, blank=True, default='')
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=False, blank=True)

    def __str__(self):
        return self.title


class Vehicle(models.Model):
    model_name = models.CharField(max_length=100, blank=False, default='')
    subtitle = models.CharField(max_length=150, blank=True, default='')
    description = models.TextField(null=True, blank=True)
    type = models.IntegerField(choices=TYPES, default=1)
    year = models.IntegerField(blank=False, default=0)
    price = models.IntegerField(blank=False, default=0)
    image = models.ImageField(upload_to='images/', null=False, blank=True)
    active = models.BooleanField(default=True)
    characteristics =  models.ManyToManyField(Characteristic, null=True, blank=True)

    def __str__(self):
        return self.model_name

