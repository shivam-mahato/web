from django.db import models

# Create your models here.
class Customer(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True)
    fullname=models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone = models.CharField(max_length=10)

    class Meta:
        db_table="customer"