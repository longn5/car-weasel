from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Buyer Profile
class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_subscriber = models.BooleanField(default=True)
    paid_tier = models.BooleanField(default=False)


# # https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#          Buyer.objects.create(user=instance)

# # https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.Buyer.save()