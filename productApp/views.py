from django.shortcuts import render
from .models import *
from rest_framework.viewsets import ModelViewSet
from .serializer import *
# Create your views here.
class productView(ModelViewSet):
    queryset=products.objects.all()
    serializer_class=productSerializer

class orderView(ModelViewSet):
    queryset=order.objects.all()
    serializer_class=orderSerializer


class orderItemView(ModelViewSet):
    queryset=orderItem.objects.all()
    serializer_class=orderItemSerializer



class catagoryView(ModelViewSet):
    queryset=Catagories.objects.all()
    serializer_class=catagorySerializer

class reviewView(ModelViewSet):
    queryset=review.objects.all()
    serializer_class=reviewSerializer

class wishListView(ModelViewSet):
    queryset=wishListMOdel.objects.all()
    serializer_class=wishListSerializer
