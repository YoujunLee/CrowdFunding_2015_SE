# -*- coding: utf-8 -*-
# -*- coding: euc-kr -*-

# login app ���� �κ������� �Ϸ�(2/22)


from django.contrib.auth.decorators import login_required#�α��� �����
from django.contrib.auth import logout #�α׾ƿ� ���
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q #������ ���̽� OR ��� ����

from login.models import Profile    # ȸ�� �߰� ���� model
from django.contrib.auth.models import User    # user model ���
from write.models import *

def main(request):
    try:
            write = WriteData.objects.filter()[0]
    except:
            write=None
    return render_to_response("html/index.html",{"user" : request.user,"write":write})
@csrf_exempt
def LoginCheck(request):

    ##�α��� �Ҷ� üŷ�ϴ� �κ�
    if request.method == 'POST':
            username = request.POST['id']
            password = request.POST['password']
            
            try:
                user = authenticate(username=username, password=password)
                if user is not None:
                    auth_login(request, user)
                    try:
                         write = WriteData.objects.all()[0]
                    except:
                        write=None
                    return render_to_response("html/index.html",{"user" : request.user,"write":write})
                else:
                    return HttpResponseRedirect("/Login")
              
            except:
                  return HttpResponseRedirect("/Login")
            
    else:
            return HttpResponseRedirect("/Login")
def login(request):
    if request.user.username == "":
        return render_to_response('html/login.html')
    else:
        return HttpResponseRedirect("/")
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

def RegisterGo(request):
    return render_to_response('html/sign_up.html')

@csrf_exempt
def Register(request):
    if request.method=='POST':
        Name = request.POST['inputName']
        stu_num = request.POST['inputStudentId']
        Phone =request.POST['Phone']
        password = request.POST['inputPassword']
        question = request.POST['question']
        answer = request.POST['answer']
        
        try:
            user = User.objects.create_user(username=stu_num, password=password, email="")
            user.save()
            get_user = User.objects.get(username=stu_num)
            
            profile = Profile(User=get_user, Name=Name, phone=Phone, hint=question, answer=answer)
            profile.save()
            
            return render_to_response('html/login.html')


        except:
            return HttpResponseRedirect("/Register")
        