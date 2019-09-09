from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


from .models import Seller, SellerPost

class SellerAdmin(admin.ModelAdmin):
    empty_value_display = '--empty--'
    list_display = ('seller_name', 'bis_name', 'street', 'city', 'state', 'zipcode')


class SellerPostAdmin(admin.ModelAdmin):
    empty_value_display = '--empty--'
    list_display = (
        'userid',
        'cylinders',
        'doors',
        'drive',
        'make',
        'model',
        'series',
        'trim',
        'vin',
        'year'
    )


admin.site.register(Seller, SellerAdmin)
admin.site.register(SellerPost, SellerPostAdmin)