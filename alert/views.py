from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User
from django.contrib.auth import authenticate,logout,login

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
        # user = authenticate(request, phone=phone, password=password)
        # print(user)

        print(res)
        if len(res) == 1:
            return render(request,"home.html")
        else:
            # print("here")
            context = {"message":"credential invalid"}
            return render(request,"index.html",context)
    else:
        return HttpResponse("ok")



def services(request):
    return render(request,"services.html")

def logout(request):
    logout(request)
    return redirect
