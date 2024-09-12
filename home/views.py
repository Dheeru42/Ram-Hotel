from django.shortcuts import render,redirect
from home.models import Book,Contact
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login

def index(request):
    if request.user.is_anonymous:
        return render(request,'logi.html')
    return render(request,'index.html')

def cont(request):
    if request.user.is_anonymous:
        return render(request,'logi.html')
    if request.method == 'POST':
        fname = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mob')
        cont = Contact(name=fname,email=email,phone=mobile,date=datetime.now())
        cont.save()
        messages.success(request, "Your Message is Sent")
    return render(request,'cont.html')

def logi(request):
    if request.method=='POST':
        uname = request.POST.get('username')
        passw = request.POST.get('password')
        user = authenticate(username=uname, password=passw)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return render(request,"logi.html")
    return render(request,"logi.html")

def logo(request):
    logout(request)
    return redirect('/logi')

def ord(request):
    if request.user.is_anonymous:
        return render(request,'logi.html')
    if request.method == 'POST':
        fname = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('num')
        checkin = request.POST.get('checkin')
        checkout = request.POST.get('checkout')
        nguest = request.POST.get('guests')
        rtype = request.POST.get('room')
        book = Book(name=fname,email=email,phone=mobile,checkindate=checkin,checkoutdate=checkout,
                    nguest=nguest,rtype=rtype)
        book.save()
        messages.success(request, "Your Booking is Complete")
    return render(request,'order.html')
