from django.db import models

# Create your models here.
class FIR(models.Model):
    unique_id = models.CharField(max_length=100)
    name =models.CharField(max_length=100)
    accused_name =models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    description =models.TextField()
    date_added =models.DateField(auto_now_add=True)
    image =models.ImageField(upload_to="media")
    def __str__(self):
        return self.accused_name
