from django.db import models

# Create your models here.


class customer(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    phone_number = models.CharField(max_length=20, blank=False, null=False)
    sex = models.CharField(max_length=2, blank=False, null=False)
    birth = models.CharField(max_length=8, blank=False, null=False, default='19000101')
    address = models.CharField(max_length=100, blank=False, null=False, default='')
    car_number = models.CharField(max_length=20, null=True, blank=True)
    etc = models.CharField(max_length=100, null=True, blank=True)