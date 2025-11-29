


from django.db import models

# Create your models here.
class Registrations(models.Model):
    Rid=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=30)
    Email=models.EmailField(max_length=50)
    Password=models.CharField(max_length=15)
    Gender=models.CharField(max_length=30)
    College=models.CharField(max_length=30)
    Mobile=models.BigIntegerField()

class Login(models.Model):
    Email=models.EmailField(max_length=50)
    Pass=models.CharField(max_length=15)