from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Buyer, BuyerPost

class BuyerAdmin(admin.ModelAdmin):
    empty_value_display = '--empty--'
    list_display = ('buyer_name', 'buyer_email', 'is_subscriber', 'paid_tier')

class BuyerPostAdmin(admin.ModelAdmin):
    empty_value_display = '--empty--'
    list_display = ('userid', 'make', 'model', 'year')


admin.site.register(Buyer, BuyerAdmin)
admin.site.register(BuyerPost, BuyerPostAdmin)