from django.db import models

# Create your models here.
class FIR(models.Model):
    name =models.CharField(max_length=100,blank=True,null=True)
    age = models.CharField(max_length=100,blank=True,null=True)
    address = models.CharField(max_length=100,blank=True,null=True)
    station_code  = models.CharField(max_length=100,blank=True,null=True)
    state = models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return self.accused_name
