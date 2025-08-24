from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import userApiView
router=DefaultRouter()
router.register(r'user', userApiView) 

urlpatterns = [
    path('api/',include(router.urls))
]
