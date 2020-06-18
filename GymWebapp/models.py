from django.db import models
from datetime import date, datetime
# Create your models here.
class Packages(models.Model):
    package_type = models.CharField(max_length=10)
    cost = models.BigIntegerField()

    def __str__(self):
        return self.package_type

class Subscription(models.Model):
    start_date = models.DateField(auto_now_add=True,auto_now=False,blank=True)
    end_date = models.DateField(auto_now_add=False,auto_now=False,blank=True)
    payment = models.BigIntegerField()
    customer = models.ForeignKey('Customer_Details',on_delete=models.CASCADE)
    package = models.ForeignKey('Packages',on_delete=models.CASCADE)
    pay_check= models.BooleanField(default=False)
    def __str__(self):
        cus = str(self.customer)
        return cus

class Customer_Details(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=200)
    PhoneNumber = models.BigIntegerField()
    password = models.CharField(max_length=120)
    gender = models.CharField(max_length=10)
    def __str__(self):
        return self.username

class Workoutplan(models.Model):
    Dietplan = models.TextField()
    Exercise = models.TextField()
    Customer = models.ForeignKey('Customer_details',on_delete=models.CASCADE)
    def __str__(self):
        cus = str(self.Customer)
        return cus




