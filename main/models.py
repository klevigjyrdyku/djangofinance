from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    groups = models.ManyToManyField(Group, related_name='custom_users')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


class Transaction(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    payer_payee = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=50)
    reference_number = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    attachments = models.FileField(upload_to='attachments/', blank=True)
    photo = models.ImageField(upload_to='transaction_pics', null=True, blank=True)  # shto fushen photo


    def __str__(self):
        return self.description
