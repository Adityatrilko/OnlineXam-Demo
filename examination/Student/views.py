



from django.shortcuts import render,redirect,HttpResponse
import datetime
from .models import Registrations
from Exam.models import Question,Test
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def Register(request):
    if request.method=='POST':
        Name=request.POST['Name']
        Email=request.POST['Email']
        Password=request.POST['Password']
        Gender=request.POST['Gender']
        College=request.POST['College']
        Mobile=request.POST['Mobile']
        Usr=Registrations(Name=Name,Email=Email,Pass=Password,Gender=Gender,College=College,Mobile=Mobile)
        user=User.objects.create_user(username=Email,password=Password)
        Usr.save()
        user.save()
        return redirect('/login')
    
    return render(request,'Registration.html')

def Login(request):
    if request.method=='POST':
        Email=request.POST['Email']
        Pass=request.POST['Pass']
        data=Registrations.objects.get(Email=Email)
        user=authenticate(username=Email,password=Pass)
        if (user):
            login(request,user)
            return redirect('/Studenthome/'+str(data.Rid))
        else:
            return HttpResponse('Invalid username or Password')    

    return render(request,'login.html')

def logout(request):
    logout(request)
    return redirect('/login')

def Studenthome(request,Rid):
    data=Registrations.objects.get(Rid=Rid)
    if request.method=='POST':
        qtype=request.POST['Paper']
        d=datetime.date.today()
        try:
            test=Test.objects.get(Sid=Rid,Qpapertype=qtype,Date=d)
            return HttpResponse('You Have already taken This Test')
        except ObjectDoesNotExist:
            q=Question.objects.filter(Qtype=qtype).first()
            return redirect('/Questionpaper/'+str(Rid)+'/'+qtype+'/'+str(q.Qid))
    return render(request,'Userhome.html',{'data':data})

def About(request):
    return render (request,'Aboutus.html')

def Contact(request):
    return render(request,'Contactus.html')