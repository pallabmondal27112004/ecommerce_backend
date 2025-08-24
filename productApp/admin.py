from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Catagories)
admin.site.register(products)
admin.site.register(order)
admin.site.register(orderItem)
admin.site.register(review)
admin.site.register(wishListMOdel)