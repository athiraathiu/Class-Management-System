from django.db import models

# Create your models here.

class qualification(models.Model):
    qual_name=models.CharField(max_length=255)
    
class Designation(models.Model):
    desg_name=models.CharField(max_length=255)
    desg_code=models.CharField(max_length=255)
    
class Addcls(models.Model):
    cls=models.CharField(max_length=50)
    
class Add_div(models.Model):
    div=models.CharField(max_length=50)
    
class Category(models.Model):
    cat_name=models.CharField(max_length=100)
    
class Product(models.Model):
    c_id=models.ForeignKey("Category",on_delete=models.CASCADE)
    itm=models.CharField(max_length=100)
  
