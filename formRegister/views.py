from tabnanny import check
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import JsonResponse
import pymongo

myclient = pymongo.MongoClient("mongodb://santi:Santi!12321@157.245.59.56:27018/?authSource=admin&readPreference=primary&directConnection=true&ssl=false")
def check_register(lineID):
    query={
        'lineID': lineID
    }
    mycol = myclient['LPR']['register']
    if mycol.find_one(query)!=None:
        return True
    else:
        print('Line_User_Id : ซำ้าๆๆๆๆๆ')
        return False
def insert_data(lineID,name,license_plate,tel,email):
    if check_register(lineID):
        mydb = myclient["LPR"]
        mycol = mydb["register"]
        mydict = { 
            "Line_Users_ID": lineID,
            'name': name,
            'license_plate': license_plate,
            'tel': tel,
            'Email':email
        }
        mycol.insert_one(mydict)

def index(request):
    if request.is_ajax():
        print('เป็น Ajax')
        if 'lineID' in request.GET:
            lineID = request.GET['lineID']
            name = request.GET['name']
            license_plate = request.GET['license_plate']
            tel = request.GET['tel']
            email = request.GET['Email']
            print('Line user id :', lineID)
            insert_data(lineID,name,license_plate,tel,email)
            return JsonResponse({
            "Line_Users_ID": lineID,
            'name': name,
            'license_plate': license_plate,
            'tel': tel,
            'Email':email
            })
        else:
            print('ไม่มี lineID เข้ามา')
    else:
        print('ไม่ใช่ Ajax')
    return render(request,'index.html',)

def webhook(request):
     if request.method == 'POST':
        name = request.POST.get('name','ไม่มีชื่อส่งมา')
        license_plate = request.POST.get('license_plate','ไม่มีชื่อส่งมา')
        tel = request.POST.get('tel','ไม่มีชื่อส่งมา')
        Email = request.POST.get('Email','ไม่มีชื่อส่งมา')
        var = {
            'name': name,
            'license_plate': license_plate,
            'tel': tel,
            'Email':Email
        }
        return render(request,'index.html',var)

