from django.db import models

# Create your models here.

class User(models.Model):
    userType = [
        ('normal', 'Normal'),
        ('staff', 'Staff'),
	]
    phone = models.CharField(max_length=50,blank=False,default="")
    name = models.CharField(max_length=50,blank=False,default="")
    password = models.CharField(max_length=100,blank=False,default="")
    type = models.CharField(max_length=200,choices=userType,default="")


    def __str__(self):
        return f"{self.phone} - {self.name}"

class ServiceType(models.Model):
    stype = models.CharField(max_length=100)
    def __str__(self):
        return self.stype

class Service(models.Model):
    name = models.CharField(max_length=100)
    serviceType = models.ForeignKey(ServiceType,on_delete=models.CASCADE)
    serviceDesc = models.TextField(max_length=500)

    def __str__(self):
        return self.name


