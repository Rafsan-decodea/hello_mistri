from django.http import response
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import backends, logout as user_logout
from .models import *


def index(request):
    
    return render(request,"index.html")

def dashboard(request): 
   
    return render(request ,"dashboard/index.html")

def insert_data(request):
     admin = Admin.objects.all()
     context = {
        "admin" : admin,
       }
     return render(request,"dashboard/data_entry.html",context)


def information(request):
    #{{user.social_auth.get.provider}} {{ user.social_auth.get.uid }}

    return render(request,"information.html")

def insert_clint_information(request):
    if request.method == 'POST':
         clint = ClientInformation()
         clint.clint_id = request.POST.get('clint_id') 
         clint.name= request.POST.get('name')
         clint.phone= request.POST.get('phone')
         clint.address = request.POST.get('address')
         print (request.POST.get('clint_id'))
         print (request.POST.get('name'))
         print ( request.POST.get('phone'))

         clint.save()
         
         
        
    return render(request,"dashboard/index.html")

def insert_mistri_information(request):
    if request.method == 'POST':
         mistri = MistriInformation()
         mistri.mistri_id = request.POST.get('mistri_id')
         mistri.name = request.POST.get('name')
         mistri.phone = request.POST.get('phone')
         mistri.image = request.FILES['image']  
         mistri.address = request.POST.get('address')
         mistri.dob = request.POST.get('dob')
         mistri.save()
         
    
    return render(request,"dashboard/index.html")
    


def logout(request):
    user_logout(request)
    return render(request,"index.html")
# Create your views here.
