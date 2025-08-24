from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import productView,orderView,orderItemView,reviewView,catagoryView, wishListView
router = DefaultRouter()
router.register(r'product', productView) 
router.register(r'order', orderView) 
router.register(r'orderitem', orderItemView) 
router.register(r'review', reviewView) 
router.register(r'catagory', catagoryView,basename="category")  
router.register(r'wishlist', wishListView )
urlpatterns = [
    path('api/', include(router.urls)), 
]


