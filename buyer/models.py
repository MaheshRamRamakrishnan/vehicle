from django.db import models

# Create your models here.
class buyerregistration(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phonenumber = models.PositiveBigIntegerField(null=True)
    gender = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200)

class buyer_data(models.Model):
    first_name = models.CharField(max_length=200,  null=True)
    last_name = models.CharField(max_length=200,  null=True)
    email = models.EmailField(unique=True)
    employment = models.CharField(max_length=200,  null=True)
    number = models.CharField(max_length=200,  null=True)
    gender = models.CharField(max_length=200,  null=True)
    city = models.CharField(max_length=200,  null=True)
    car_type = models.CharField(max_length=200,  null=True)
    fuel = models.CharField(max_length=200,  null=True)
    transmission = models.CharField(max_length=200,  null=True)
    No_of_Owners = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200,  null=True)
