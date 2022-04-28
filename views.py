from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User
from django.core.mail import EmailMessage



def index(request):
    return render(request,"signin.html",{})

def register(request):
    return render(request,"signup.html", {})

def forgot(request):
    return render(request,"forgot.html",{})

def registeration(request):
    name = request.POST['name']
    email = request.POST['email']
    mobile = request.POST['mobile']
    pw = request.POST['password']
    data = User.objects.all()
    print(data)
    print(mobile)
    obj=User(name=name,email=email,password=pw,mobilenumber=mobile)
    obj.save()
    return HttpResponse("Your details stored sucessfully !!!")
def checkuser(request):
    email = request.POST['email']
    password = request.POST['password']
    print(email)
    print(password)
    x = User.objects.filter(email=email).filter(password=password).count()
    print(x)
    if x>=1:
        request.session['email'] = email
        return HttpResponse("Login Successful!")
    else:
        return redirect("index")


def sendotp(request):
    email=request.POST['email']
    obj=EmailMessage("Test Mail","Thanks for contacting me",to=[email])
    obj.send()
    return HttpResponse("OTP sent successfully!")