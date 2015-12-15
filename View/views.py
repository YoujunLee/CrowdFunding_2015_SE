# -*- coding: utf-8 -*-
# -*- coding: euc-kr -*-

from django.shortcuts import render
from write.models import *
from django.shortcuts import render_to_response
# Create your views here.
def viewData(request,offset): #메인페이지에서 view detail를 눌렀을 때 나오는 것
	write = WriteData.objects.get(id=offset)
	per = (float(write.putmoney)/float(write.money))*100
	return render_to_response("html/bullet.html",{"user",request.user,"write" : write,"per":float(per)})
def WriteInfo(request,offset): #결재하기 누른 후에 페이지를 보여주기 위한 함수
	write = WriteData.objects.get(id=offset)
	return render_to_response("html/input.html",{"write":write})
