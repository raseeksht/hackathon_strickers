from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import User,Report,OrgUser
from django.views.decorators.csrf import csrf_exempt
import json
import jwt
from django.db.models import Q
from django.core import serializers
from django.shortcuts import get_object_or_404
from .message import message


JWT_SECTET = "secret"

# Create your views here.

@csrf_exempt
def login(request):
     if request.method == 'POST':
        
        jsonbody = json.loads(request.body)
        print(jsonbody)
        # return HttpResponse("ok")

        if jsonbody['userType'] == "normal":
            res = User.objects.filter(phone=jsonbody['phone'],password=jsonbody['passwd'])
        else:
            res = OrgUser.objects.filter(phone=jsonbody['phone'],password=jsonbody['passwd'])
        
        
        if len(res) == 1:
            jwt_encoded = jwt.encode({"phone": jsonbody['phone']}, JWT_SECTET, algorithm="HS256")
            print(jwt_encoded)
        # return HttpResponse("ok")
            # const usertype = (jsonbody['userType'] == "normal") ? res[0].type : res[0].orgType
            
            if jsonbody['userType'] == "normal":
                usr = res[0].type
            else:
                usr = res[0].orgType

            response = {"token":jwt_encoded,
                        "name":res[0].name,
                        "phone":jsonbody['phone'],
                        "userType":usr}
            return JsonResponse({"message":"login_success","data":response})
        else:
            return JsonResponse({"message":"invalid credential"})
            
        #     return response
        # else:
        #     # print("here")
        #     return JsonResponse({"message":"invalid login"})


def index(request):
    return render(request,"index.html")

def home(request):
    return render(request,"home.html")



def services(request):
    return render(request,"services.html")

@csrf_exempt
def report(request):
    if request.method == "POST":
        jsondata = json.loads(request.body)
        print(jsondata)
        newrecord = Report(reportType=jsondata['reportType'],Desc=jsondata['medDesc'],Type=jsondata['medType'],latitude=jsondata['location']['latitude'],longitude=jsondata['location']['longitude'],reportedBy=jsondata['reportedBy'])
        newrecord.save()
        message(jsondata['location']['latitude'],jsondata['location']['longitude'],alert=jsondata['reportType'],desc=jsondata['medDesc'])
        
    
        return JsonResponse({"message":"Case Reported"})

    

def checkToken(request):
    headers = request.headers
    print("here")
    jwttoken = headers.get("Authorization")

    try:
        decoded = jwt.decode(jwttoken, JWT_SECTET, algorithms=['HS256'])
        print(decoded)

        # The token is valid, and the payload is available in decoded_payload
        return JsonResponse({"message":"valid_token"})
    except Exception:
        return JsonResponse({"message":"invalid_token"})


def signup(request):
    return render(request,"signup.html")


@csrf_exempt
def register(request):
    if request.method == "POST":
        jsondata = json.loads(request.body)
        print(jsondata)
        if jsondata['userType'] == "normal":
            newuser = User(phone=jsondata['phone'],
                       name=jsondata['name'],
                       password=jsondata['passwd'],
                       type=jsondata['userType'])
        else:
            newuser =OrgUser(phone=jsondata['phone'],
                       name=jsondata['name'],
                       password=jsondata['passwd'],
                       type=jsondata['userType'],
                       orgType=jsondata['orgType']
                       )
        newuser.save()
        jwt_encoded = jwt.encode({"phone": jsondata['phone']}, JWT_SECTET, algorithm="HS256")

        payload = {"token":jwt_encoded,"name":jsondata['name'],"phone":jsondata['phone'],"userType":jsondata['userType']}
        return JsonResponse({"message":"register_success","data":payload})
    else:
        return HttpResponse("Method not allowed")


def pendingcase(request):
    return render(request,"pendingcases.html")

@csrf_exempt
def fetchpendingcase(request):
    if request.method =="POST":
        jsondata = json.loads(request.body)
        print(jsondata)
        if jsondata['userType'] == "police":
            reports = Report.objects.exclude(status="resolved")
        elif jsondata['userType']=="normal":
            reports = Report.objects.filter(
                reportedBy=jsondata['phone']
            )
        else:
            reports = Report.objects.filter(
            ~Q(status="resolved") & Q(reportType="medical")
            )
        data = serializers.serialize("json", reports)
        print(data)
        return JsonResponse({"message":"ok","data":data})


def acknowledge(request):
    ack = request.GET.get('ack', None)
    name = request.GET.get('name', None)
    # set acknowledge by the organication
    if ack is not None:
        report = get_object_or_404(Report, pk=ack)

        report.status = f"Acknowledged by {name}"
        report.save()

        return JsonResponse({"message": "acknowledge_okay"})
    else:
        return JsonResponse({"message": "acknowledge_failed"})

def resolve(request):
    ack = request.GET.get('ack', None)
    # set acknowledge by the organication
    if ack is not None:
        report = get_object_or_404(Report, pk=ack)

        report.status = f"resolved"
        report.save()

        return JsonResponse({"message": "resolve_okay"})
    else:
        return JsonResponse({"message": "resolve_failed"})