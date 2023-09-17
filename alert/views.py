from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import User,Report,OrgUser
from django.views.decorators.csrf import csrf_exempt
import json
import jwt


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

            response = {"token":jwt_encoded,"name":res[0].name,"phone":jsonbody['phone'],"userType":res[0].type}
            return JsonResponse({"message":"login_success","data":response})

            
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
    pass