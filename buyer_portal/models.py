from django.db import models
from django.contrib.auth.models import User

# Buyer Profile
class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_subscriber = models.BooleanField(default=True)
    paid_tier = models.BooleanField(default=False)
