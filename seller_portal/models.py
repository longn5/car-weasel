from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Seller Profile
class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bis_name = models.CharField(max_length=100, blank=False, null=False)
    street = models.CharField(max_length=100, blank=False, null=False)
    city = models.CharField(max_length=100, blank=False, null=False)
    state = models.CharField(max_length=2, blank=False, null=False)
    zipcode = models.CharField(max_length=5, blank=False, null=False)

    def __str__(self):
        return self.bis_name

    def seller_name(self):
        return self.user.first_name + ' ' + self.user.last_name

# # https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Seller.objects.create(user=instance)

# # https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.Seller.save()