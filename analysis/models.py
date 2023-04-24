from django.db import models


# Create your models here.
class analysisregistration(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phonenumber = models.PositiveBigIntegerField(null=True)
    gender = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200)


class team_details(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    eid = models.CharField(max_length=200)
    gender = models.CharField(max_length=200,null=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    pin = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    team_no = models.CharField(max_length=200)


class mechanical_analysis(models.Model):
    car_name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    km = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    engine = models.CharField(max_length=200)
    condition = models.CharField(max_length=200)
    gear = models.CharField(max_length=200)
    gear_condition = models.CharField(max_length=200)
    air_bag = models.CharField(max_length=200)
    airbag_condition = models.CharField(max_length=200)
    tyre_condition = models.CharField(max_length=200)
    light_condition = models.CharField(max_length=200)
    comment = models.CharField(max_length=200)
    quotation = models.IntegerField(null=True)
    to_seller = models.BooleanField(default=False)
    accept = models.BooleanField(default=False)
    deny = models.BooleanField(default=False)
    smart_contract = models.BooleanField(default=False)
    bid = models.IntegerField(max_length=200, null=True)
    car_encrypt = models.CharField(max_length=500, null=True)
    condition_encrypt = models.CharField(max_length=500, null=True)
    gear_condition_encrypt = models.CharField(max_length=500, null=True)
    km_encrypt = models.CharField(max_length=500, null=True)
    year_encrypt = models.CharField(max_length=500, null=True)
    hash_id = models.CharField(max_length=500, null=True)
