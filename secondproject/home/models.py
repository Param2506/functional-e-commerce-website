from django.db import models
from datetime import datetime
from django.utils import timezone
from django.utils.timezone import now

# Create your models here.
class Product(models.Model):
    Category=models.CharField(max_length=40, default="")
    product_id= models.AutoField
    product_name=models.CharField(max_length= 20, default="")
    product_image=models.ImageField(upload_to="home/images", default="")
    price=models.IntegerField(default=0)
    description= models.CharField(max_length= 300 , default='')
    pub_date=models.DateField(auto_now_add=True)


    def __str__(self):
        return self.product_name

class Contact(models.Model):
    query_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, default='')
    email = models.EmailField(max_length=254, default='')
    phone = models.IntegerField(default='')
    address = models.CharField(max_length=100, default='')
    state = models.CharField(max_length=40, default='')
    city = models.CharField(max_length=40, default='')
    pincode = models.IntegerField( default='')
    textarea = models.CharField( max_length=400 ,default='')

    def __str__(self):
        return self.name
    
class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    jsonitems = models.CharField(max_length=5000, default="")
    name = models.CharField(max_length=20, default='')
    email = models.EmailField(max_length=254, default='')
    phone = models.IntegerField(default='')
    address = models.CharField(max_length=100, default='')
    state = models.CharField(max_length=40, default='')
    city = models.CharField(max_length=40, default='')
    zipcode = models.IntegerField( default='')
    
    def __str__(self):
        return self.name

class orderupdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.CharField(max_length=10)
    update_desc = models.CharField(max_length=200)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:5]+"..."
