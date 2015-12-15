from django.shortcuts import render
from write.models import *
from django.shortcuts import render_to_response
# Create your views here.
def viewData(request,offset):
	write = WriteData.objects.get(id=offset)
	per = (float(write.putmoney)/float(write.money))*100
	return render_to_response("html/bullet.html",{"write" : write,"per":float(per)})
def WriteInfo(request):
	return render_to_response("html/input.html")
