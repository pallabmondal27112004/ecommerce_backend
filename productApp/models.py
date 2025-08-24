from django.db import models
from django.contrib.auth.models import User
from userApp.models import CustomerUser

# Create your models here.
class Catagories(models.Model):
    name=models.CharField(max_length=50,null=True,blank=True)
    image=models.ImageField(null=True, blank=True, upload_to='category_image/' )
    def __str__(self):
        return self.name
class products(models.Model):
    user=models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    name=models.CharField(max_length=50, null=True, blank=True)
    image=models.ImageField(null=True,blank=True, upload_to='product_image/')
    brand=models.CharField(max_length=50, null=True, blank=True)
    catagory= models.ForeignKey(Catagories,on_delete=models.CASCADE, null=True,blank=True,)
    description=models.CharField(max_length=50,null=True,blank=True)
    offer=models.IntegerField(null=True, blank=True)
    isFreeDelevary=models.BooleanField(default=False, null=True, blank=True)
    rating=models.DecimalField(max_digits=10, decimal_places=1, null=True,blank=True )
    numOfReview=models.IntegerField(null=True,blank=True,default=0)
    price=models.DecimalField(max_digits=10, decimal_places=2, null=True,blank=True)
    countInStack=models.IntegerField(null=True,blank=True)
    createdAt=models.DateTimeField(auto_now=True,null=True,blank=True,)

    def __str__(self):
        return self.name
        

class review(models.Model):
    product=models.ForeignKey(products, on_delete=models.CASCADE,null=True,blank=True)
    user=models.ForeignKey(CustomerUser,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=500,null=True,blank=True)
    rating=models.IntegerField(null=True,blank=True)
    comment=models.CharField(max_length=300,null=True,blank=True)
    createdAt=models.DateTimeField(auto_now=True,null=True,blank=True,)

    def __str__(self):
        return self.product.name, self.user
    
class order(models.Model):
    user=models.ForeignKey(CustomerUser ,on_delete=models.CASCADE,null=True,blank=True)
    paymentMethod=models.CharField(max_length=50,null=True,blank=True)
    taxPrice=models.DecimalField(max_digits=10, decimal_places=2, default=0,null=True,blank=True,)
    shippingPrice=models.DecimalField(max_digits=10, decimal_places=2, default=0,null=True,blank=True)
    totalprice=models.DecimalField(max_digits=10, decimal_places=2, default=0,null=True,blank=True)
    isPaid=models.BooleanField(default=False,null=True,blank=True,)
    paidAt=models.DateTimeField( auto_now_add=True,null=True,blank=True)
    isDelevary=models.BooleanField(default=False,null=True,blank=True)
    delevaryAt=models.DateTimeField(auto_now_add=True,null=True,blank=True,)
    createdAt=models.DateTimeField(auto_now_add=True,null=True,blank=True,)

    def __str__(self):
        return self.user.last_name+self.user.last_name , self.totalprice

class orderItem(models.Model):
    product=models.ForeignKey(products,on_delete=models.CASCADE,null=True, blank=True)
    # orders=models.ForeignKey(order, on_delete=models.CASCADE, null=True, blank=True,)
    # name=models.CharField(max_length=50,null=True, blank=True)
    user=models.ForeignKey(CustomerUser, on_delete=models.CASCADE, null=True, blank=True)
    quentity=models.IntegerField(null=True, blank=True,default=0)
    price=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return  self.product.name


class wishListMOdel(models.Model):
    product= models.ForeignKey(products, on_delete= models.CASCADE, null= True, blank=True)
    user=models.ForeignKey(CustomerUser, on_delete=models.CASCADE, null=True, blank=True)
    iswishlist=models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return "Wish List" + self.product.name
    