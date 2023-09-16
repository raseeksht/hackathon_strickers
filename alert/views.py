from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import User,Service
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
    service = Service.objects.all()
    context = {"service":service}
    return render(request,"services.html",context)

@csrf_exempt
def report(request):
    if request.method == "POST":
        # print(request.body)
        jsondata = json.loads(request.body)
        print(jsondata)
        return JsonResponse({"message":"Case Reported"})

