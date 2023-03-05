from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, update_session_auth_hash, logout
from .forms import SignUpForm
from django.conf import settings
from django.core.mail import send_mail
import math, random
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from .models import Transport

# Create your views here.

def generateOTP() :
 
    # Declare a digits variable 
    # which stores all digits
    digits = "0123456789"
    OTP = ""
 
   # length of password can be changed
   # by changing value in range
    for i in range(4) :
        OTP += digits[math.floor(random.random() * 10)]
 
    return OTP

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            passcode = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=passcode)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request,'signup.html',{'form': form})

def signin(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, 'signin.html')
    return render(request, 'signin.html')

def check_email(request):
    if request.method=="POST":
        mail = request.POST.get('email_id')
        subject = 'Request for password change'
        code = generateOTP()
        message = 'Verification code for password change\n'+code
        email_from = settings.EMAIL_HOST_USER
        send_mail(subject,message,email_from,mail)
        return redirect('/changepassword',code)
    return render(request,'ForgotPassword.html')
        

def change_password(request, code):
    if request.method=="POST":
        getotp = request.POST.get('otp')
        if getotp==code:
            form = PasswordChangeForm(request.user,request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request,user)
                messages.success(request, 'Your password was successfully updated!')
                return redirect('/changepassword')
            else:
                messages.error(request, 'Please correct the error below')
        else:
            messages.error(request,'Enter the correct OTP')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'ChangePassword.html',{'form': form})

def list(request):
    starting_point = request.POST.get('sp')
    ending_point = request.POST.get('ep')
    day = request.POST.get('day')
    a = Transport.objects.all()
    par = {'detail': a,'startpt': starting_point,'endpt': ending_point,'dt':day}
    return render(request,'List.html',par)