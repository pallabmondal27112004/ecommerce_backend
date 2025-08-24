from rest_framework import serializers
from .models import *
class shippingAddressSerilizer(serializers.Serializer):
    class Meta:
        model=shippingAddress
        fields='__all__'
        