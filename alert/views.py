from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import User,Report
from django.views.decorators.csrf import csrf_exempt
import json
import jwt


JWT_SECTET = "secret"

# Create your views here.

def login(request):
    return render(request,"index.html")

def authenticate():
    pass
     

def home(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        res = User.objects.filter(phone=phone,password=password)
        # user = authenticate(request, username=username, password=password)
        # print(user)

        print(res)
        if len(res) == 1:
            jwt_encoded = jwt.encode({"phone": phone}, JWT_SECTET, algorithm="HS256")

            response = render(request,"home.html",context={"jwt":jwt_encoded})
            response['Authorization'] = jwt_encoded
            return response
        else:
            # print("here")
            context = {"message":"credential invalid"}
            return render(request,"index.html",context)
    else:
        return render(request,"home.html")



def services(request):
    return render(request,"services.html")

@csrf_exempt
def report(request):
    if request.method == "POST":
        jsondata = json.loads(request.body)
        print(jsondata)
        newrecord = Report(reportType=jsondata['reportType'],Desc=jsondata['medDesc'],Type=jsondata['medType'],latitude=jsondata['location']['latitude'],longitude=jsondata['location']['longitude'])
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
        newuser = User(phone=jsondata['phone'],
                       name=jsondata['name'],
                       password=jsondata['passwd'],
                       type=jsondata['userType'])
        newuser.save()
        return JsonResponse({"message":"register is here baby"})
    else:
        return HttpResponse("Method not allowed")