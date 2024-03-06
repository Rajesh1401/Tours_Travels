from django.db import models
class Login(models.Model):
    lemail=models.CharField(max_length=15)
    lpassword=models.CharField(max_length=16)

class Contactus(models.Model):
    customer_name=models.CharField(max_length=20)
    mobile_number=models.CharField(max_length=10)
    email_id=models.CharField(max_length=20)
    query_text=models.CharField(max_length=100)

class Booking(models.Model):
    location=models.CharField(max_length=20)
    destination=models.CharField(max_length=20)

class Payment(models.Model):
    name=models.CharField(max_length=20)
    card=models.CharField(max_length=10)
    number =models.CharField(max_length=10)
    expiry =models.CharField(max_length=4)
    ccv=models.CharField(max_length=3)

class Signin(models.Model):
    suname=models.CharField(max_length=20)
    suemail=models.CharField(max_length=15)
    supassword=models.CharField(max_length=16)


# Create your models here.
