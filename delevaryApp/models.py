from django.db import models
from productApp.models import order
# Create your models here.
class shippingAddress(models.Model):
    orders=models.ForeignKey(order, on_delete=models.CASCADE,null=True, blank=True)
    address=models.CharField(max_length=500,null=True, blank=True)
    city=models.CharField(max_length=50,null=True, blank=True)
    postalCode=models.CharField(max_length=50,null=True, blank=True)
    country=models.CharField(max_length=40,null=True, blank=True)
    shippingPrice=models.IntegerField(null=True, blank=True,default=0)

    def __str__(self):
        return self.address