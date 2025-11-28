from django.db import models
from django.contrib import admin
# Create your models here.
class Customer(models.Model):
    customer_id =models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id','name','email','phone')