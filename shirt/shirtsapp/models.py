from django.db import models

# Create your models here.
class Decoration(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True)
    name=models.CharField(max_length=200)
    price = models.CharField(max_length=100, default="0")
    image=models.FileField(upload_to='shirtimages',default="test decor image")

    class Meta:
        db_table="shirts"

