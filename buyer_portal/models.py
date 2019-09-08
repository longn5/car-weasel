from django.db import models
from django.contrib.auth.models import User
#from django.db.models.signals import post_save
#from django.dispatch import receiver
from django.conf import settings

# Buyer Profile
class Buyer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_subscriber = models.BooleanField(default=True)
    paid_tier = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    def buyer_name(self):
        return self.__str__()

    def buyer_email(self):
        return self.user.email

# Buyer Post
class BuyerPost(models.Model):
    userid = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    make = models.CharField(max_length=30, null=False, blank=False)
    model = models.CharField(max_length=30, null=False, blank=False)
    year = models.CharField(max_length=4, null=False, blank=False)

    def __str__(self):
        return self.make + ' ' + self.model + ' - ' + self.year