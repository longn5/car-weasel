from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


# from .models import Buyer
# #admin.site.unregister(User)

# class BuyerInline(admin.StackedInline):
#     model = Buyer
#     can_delete = False
#     verbose_name_plural = 'Buyer'
#     fk_name = 'user'

# class CustomUserAdmin(UserAdmin):
#     inlines = (BuyerInline, )
    
#     def get_inline_instances(self, request, obj=None):
#         if not obj:
#             return list()
#         return super(CustomUserAdmin, self).get_inline_instances(request, obj)

# admin.site.register(User, CustomUserAdmin)