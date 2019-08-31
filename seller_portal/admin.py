from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


from .models import Seller

class SellerAdmin(admin.ModelAdmin):
    empty_value_display = '--empty--'
    list_display = ('seller_name', 'bis_name', 'street', 'city', 'state', 'zipcode')


admin.site.register(Seller, SellerAdmin)

# class SellerInline(admin.StackedInline):
#     model = Seller
#     can_delete = False
#     verbose_name_plural = 'Seller'
#     fk_name = 'user'

# class CustomUserAdmin(UserAdmin):
#     inlines = (SellerInline, )
    
#     def get_inline_instances(self, request, obj=None):
#         if not obj:
#             return list()
#         return super(CustomUserAdmin, self).get_inline_instances(request, obj)


# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)