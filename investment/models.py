from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=250, null=True)
    last_name = models.CharField(max_length=250, null=True)
    image = models.ImageField(upload_to="images", null=True, blank=True)

    def __str__(self):
       return self.user.email

class Investment(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    investment_price = models.FloatField(default=0)
    balance = models.FloatField(default=0)
    interest = models.FloatField(default=0)
    investment_plan =models.FloatField(default=0)
    wallet = models.CharField(max_length=250, null=True,blank=True)
    wallet_address= models.CharField(max_length=250, null=True,blank=True)
    amount = models.FloatField(default=0)


    def __str__(self):
        return self.user_name.username
