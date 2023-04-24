from django.db import models


# Create your models here.
class sellerregistration(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phonenumber = models.PositiveBigIntegerField(null=True)
    gender = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200)


class seller_details(models.Model):
    title = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    employment = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    Gender = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    zip = models.PositiveBigIntegerField(null=True)
    place = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    code = models.PositiveBigIntegerField(null=True)
    phone = models.PositiveBigIntegerField(null=True)
    email = models.EmailField(unique=True)
    approve = models.BooleanField(default=False)
    comment = models.CharField(max_length=200,null=True)

class vehicle_details(models.Model):
    brand = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    km_driven = models.CharField(max_length=200)
    fuel = models.CharField(max_length=200)
    transmission = models.CharField(max_length=200)
    No_of_Owners = models.CharField(max_length=200)
    Registration_City = models.CharField(max_length=200)
    car_type = models.CharField(max_length=200)
    insurance = models.CharField(max_length=200)
    rc = models.CharField(max_length=200)
    warranty = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    approve = models.BooleanField(default=False)