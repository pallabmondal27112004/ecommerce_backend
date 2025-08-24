
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
class CustomerUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    image=models.ImageField(null=True, blank= True, upload_to="user_image/" )
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    total_spent = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    wishlist = models.ManyToManyField('productApp.products', blank=True)


    groups = models.ManyToManyField(
        Group,
        related_name="customer_users",  # Avoid conflict with default User model
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customer_users_permissions",  # Avoid conflict with default User model
        blank=True
    )

    def __str__(self):
        return self.username


