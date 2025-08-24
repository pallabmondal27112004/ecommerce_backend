from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import CustomerUser
from .serializer import userSerializer
# Create your views here.
class userApiView(ModelViewSet):
    queryset=CustomerUser.objects.all()
    serializer_class=userSerializer

