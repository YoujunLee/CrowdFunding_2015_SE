from django.shortcuts import render
import json
import pycurl
import urllib
from django.shortcuts import render_to_response
from io import BytesIO
import base64
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponseRedirect
from write.models import *
# Create your views here.
@csrf_exempt
def DumpJson(request,offset):
    dicBody={}
    
    
    
    dicBody["orderNo"] = str(datetime.datetime.today());
    if request.method == "POST":
         dicBody["amount"] = request.POST['money'];
    else:
         dicBody["amount"] = 3
    dicBody["productDesc"] = "test";
    dicBody["apiKey"] = "sk_test_e3kW4mM210e3kWYV1gN1";
    dicBody["expiredTime"] = "2016-11-20 16:21:00";
    dicBody["orderCheckCallback"] = "https://http://54.64.148.172/main";
    dicBody["resultCallback"] = "https://myshop.com/toss/result.php";
    response=BytesIO()
    
    jsonBody = json.dumps(dicBody)
    curl=pycurl.Curl()
    curl.setopt(pycurl.URL,'https://toss.im/tosspay/api/v1/payments')
    curl.setopt(pycurl.WRITEFUNCTION,response.write)
    
    curl.setopt(pycurl.CUSTOMREQUEST, "POST");
    curl.setopt(pycurl.SSL_VERIFYPEER,False);
    curl.setopt(pycurl.POSTFIELDS, jsonBody);
    curl.setopt(pycurl.TRANSFERTEXT,True);
    a = []
    a.append('Content-Type: application/json')
    a.append('Content-Length: ' + str(len(jsonBody)))
    curl.setopt(pycurl.HTTPHEADER, a)
     
    curl.perform()
    
    curl.close()
    result=response.getvalue()
    result=result.decode("utf-8")
    result=json.loads(result)
    print("data : ",  result)
    print("type : ", type(result))
    write = WriteData.objects.all()[0]
    write.putmoney+=int(request.POST['money'])
    write.save()
    String='https://toss.im/tosspay/order/orderWait?payToken='+str(result['payToken'])+'&retUrl=http://54.64.148.172/main'
    

    return HttpResponseRedirect(String)
        
    
