from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q 
from write.models import WriteData
from login.models import *
from django.contrib.auth.models import User  

# Create your views here.

def write(request):
    return render_to_response("html/write.html",{"user" : request.user})

@csrf_exempt
def writeMain(request):
    if request.method=="POST":
        inputName = request.POST['inputName']
        chart = request.POST['chart']
        duedate=request.POST['duedate']
        bank=request.POST['bank']
        money=request.POST['target_money']
        text=request.POST['inputArticleContents']
        money=money.replace(",","");
        text=text.replace("\r\n","<br/>");
        
        money=int(money)
        try:
           write=WriteData.objects.get(Name=inputName);
        except:
           user=User.objects.get(username=request.user.username)
           UserData=Profile.objects.get(User=user)
           
           write=WriteData(user = UserData,Name=inputName,distribute=chart,duedate=duedate,bank=bank,money=money,text=text)
           write.save()
        
        per = (float(write.putmoney)/float(write.money))*100
        print(per)
        return render_to_response('html/bullet.html',{"user":request.user, "write":write,"per":float(per)})
        