from django.db import models



# Create your models here.
class Booking(models.Model):
    booking_id=models.AutoField(auto_created=True,primary_key=True)
    fullname = models.CharField(max_length=100)
    shirtdetails=models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    class Meta:
        db_table="booking"
