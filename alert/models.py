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

class Report(models.Model):
    reportType = models.CharField(max_length=50)
    Desc = models.CharField(max_length=200)
    Type = models.CharField(max_length=200)
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    reportedBy = models.CharField(max_length=50)

    def __str__(self):
        return self.Type + " - " + self.Desc
    
class OrgUser(models.Model):
    phone = models.CharField(max_length=50,blank=False,default="")
    name = models.CharField(max_length=50,blank=False,default="")
    password = models.CharField(max_length=100,blank=False,default="")
    type = models.CharField(max_length=200,default="")
    orgType = models.CharField(max_length=200)

    def __str__(self) :
        return self.name

    




