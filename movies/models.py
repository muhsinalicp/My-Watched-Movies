from django.db import models

# Create your models here.

class CensorInfo(models.Model):
    rating = models.CharField(max_length=25)
    certified_by = models.CharField(max_length=50)

class Movie_info(models.Model):
    title = models.CharField(max_length=25)
    year = models.IntegerField()
    summary = models.TextField()
    image = models.ImageField(upload_to='uploads/' , null=True , blank=True)
    censor_details = models.OneToOneField(CensorInfo , on_delete=models.CASCADE , null=True , blank=True)
    





