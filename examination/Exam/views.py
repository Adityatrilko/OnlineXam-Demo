



from django.shortcuts import render,redirect,HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import datetime
from .models import Question,Test
from Student.models import Registrations
# Create your views here.
def Questionpaper(request,qtype,Rid,Qid):
    stdata=Registrations.objects.get(Rid=Rid)
    Sid=Registrations.objects.get(pk=Rid)
    d=datetime.date.today()
    try:
        qdata=Question.objects.get(Qtype=qtype,Qid=Qid)
    except ObjectDoesNotExist:
            return redirect('/Result/'+str(Rid))
    if request.method=='POST':
        try:
            t=Test.objects.get(Sid=Rid,Qpapertype=qtype)
            if str(qdata.Answer)==str(request.POST['option']):
                print("next row created")
                t.Obtmarks=t.Obtmarks+4
                t.NoofRightAnswer=t.NoofRightAnswer+1
                if t.NoofRightAnswer>5:
                    t.Result='Passed'
                t.save()
        except ObjectDoesNotExist:
            if str(qdata.Answer)==str(request.POST['option']):
                qbmarks=4
                aright=1
                t1=Test(Sid=Sid,Qpapertype=qtype,Sname=stdata.Name,Maxmarks=40,Obtmarks=qbmarks,Result="Failed",Date=d,NoofRightAnswer=aright)
                t1.save()
        Qid=qdata.Qid+1
        return redirect('/Questionpaper/'+str(Rid)+'/'+qtype+'/'+str(Qid))

    return render(request,'Questionpaper.html',{'qdata':qdata,'Rid':Rid})

def Result(request,Rid):
    tdata=Test.objects.get(Sid=Rid)
    return render(request,'Result.html',{'tdata':tdata})