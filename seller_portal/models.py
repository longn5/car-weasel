from django.db import models
from django.contrib.auth.models import User

# Seller Profile
class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bis_name = models.CharField(max_length=100, blank=False, null=False)
    street = models.CharField(max_length=100, blank=False, null=False)
    city = models.CharField(max_length=100, blank=False, null=False)
    zipcode = models.CharField(max_length=5, blank=False, null=False)