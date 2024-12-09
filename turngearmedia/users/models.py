from django.db import models
from django.contrib.auth.models import AbstractUser


class Company(models.Model):
    company_name = models.CharField(max_length=120)
    address_line_1 = models.CharField(max_length=240)
    address_line_2 = models.CharField(max_length=80, null=True)
    address_state = models.CharField(max_length=80)
    address_city = models.CharField(max_length=80)
    address_zipcode = models.CharField(max_length=40)
    address_county = models.CharField(max_length=80, null=True)
    company_ein = models.CharField(max_length=240, null=True)


class User(AbstractUser):
    pass
