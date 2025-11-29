


from django.db import models
from Student.models import Registrations

# Create your models here.
class Question(models.Model):
    Qid=models.AutoField(primary_key=True)
    Qtype=models.CharField(max_length=10)
    Qdes=models.TextField(max_length=200)
    option1=models.CharField(max_length=50)
    option2=models.CharField(max_length=50)
    option3=models.CharField(max_length=50)
    option4=models.CharField(max_length=50)
    Answer=models.CharField(max_length=50)
    select=models.CharField(max_length=50)

class Test(models.Model):
    Testid=models.AutoField(primary_key=True)
    Sid=models.ForeignKey(Registrations,on_delete=models.CASCADE)
    Sname=models.CharField(max_length=30)
    Qpapertype=models.CharField(max_length=10)
    Maxmarks=models.IntegerField()
    Obtmarks=models.IntegerField()
    Result=models.CharField(max_length=10)
    NoofRightAnswer=models.IntegerField(default=0)
    Date=models.DateField(default='2020-03-01')
    class Meta:
        db_table="Test"
    
