from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
#from django.db.models.signals import post_save
#from django.dispatch import receiver

# Seller Profile
class Seller(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bis_name = models.CharField(max_length=100, blank=False, null=False)
    street = models.CharField(max_length=100, blank=False, null=False)
    city = models.CharField(max_length=100, blank=False, null=False)
    state = models.CharField(max_length=2, blank=False, null=False)
    zipcode = models.CharField(max_length=5, blank=False, null=False)

    def __str__(self):
        return self.bis_name

    def seller_name(self):
        return self.user.first_name + ' ' + self.user.last_name


# Model to represent a vehicle
class SellerPost(models.Model):
    userid = models.ForeignKey(Seller, on_delete=models.CASCADE)
    cylinders = models.CharField(max_length=1, null=True, blank=False)
    doors = models.CharField(max_length=1, null=True, blank=False)
    drive = models.CharField(max_length=60, null=True, blank=False)
    make = models.CharField(max_length=30, null=False, blank=False)
    model = models.CharField(max_length=30, null=False, blank=False)
    series = models.CharField(max_length=20, null=True, blank=False)
    trim = models.CharField(max_length=20, null=True, blank=False)
    vin = models.CharField(max_length=17, null=False, blank=False)
    year = models.CharField(max_length=4, null=False, blank=False)

    def __str__(self):
        return self.make + ' ' + self.year