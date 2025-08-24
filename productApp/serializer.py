from rest_framework import serializers
from .models import *
class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = '__all__' 
        
class orderSerializer(serializers.ModelSerializer):
    class Meta:
        model=order
        fields='__all__'

class orderItemSerializer(serializers.ModelSerializer):
    user=serializers.PrimaryKeyRelatedField(queryset=CustomerUser.objects.all())
    product = serializers.PrimaryKeyRelatedField(queryset=products.objects.all())

    class Meta:
        model = orderItem
        fields = '__all__'

    # def create(self, validated_data):
    #     """Handle nested product data during creation"""
    #     product_data = validated_data.pop('product')
    #     product, created = products.objects.get_or_create(**product_data)  # Fetch or create product
    #     order_item = orderItem.objects.create(product=product, **validated_data)  # Create order item
    #     return order_item


class catagorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Catagories
        fields='__all__'


class reviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=review
        fields='__all__'

class wishListSerializer(serializers.ModelSerializer):
    user=serializers.PrimaryKeyRelatedField(queryset=CustomerUser.objects.all())
    product = serializers.PrimaryKeyRelatedField(queryset=products.objects.all())
    class Meta:
        model=wishListMOdel
        fields='__all__'