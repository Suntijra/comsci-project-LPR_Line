from django.http import HttpResponse
from django.shortcuts import render,redirect

def registerform(request):
    return render(request,'form-html\Register.html')
    
def index(request):
    return render(request,'index.html')
def webhook(request):
    name = request.GET.get('name','ไม่มีชื่อส่งมา')
    license_plate = request.GET.get('license_plate','ไม่มีชื่อส่งมา')
    tel = request.GET.get('tel','ไม่มีชื่อส่งมา')
    Email = request.GET.get('Email','ไม่มีชื่อส่งมา')
    var = {
        'name': name,
        'license_plate': license_plate,
        'tel': tel,
        'Email':Email
    }
    return render(request,'show_get.html',var)
