from django.db import models

# Create your models here.

# from django.contrib.auth.models import AbstractUser
class Employee(models.Model):
    Employee_Name= models.CharField(max_length=20,default=0)
    Image = models.ImageField(upload_to='images')
    phone_no = models.CharField(max_length=20, default=0)
    address = models.CharField(max_length=200, default="null")
    #
    # @property
    # def imageURL(self):
    #     try:
    #         url = self.image.url
    #     except:
    #         url = ''
    #     return url

