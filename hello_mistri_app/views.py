from django.http import response
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import backends, logout as user_logout
from .models import *


def index(request):
    return render(request,"index.html")

def dashboard(request): 
    return render(request ,"dashboard/index.html")

def information(request):
    return render(request,"information.html")

def insert_clint_information(request):
    if request.method == 'POST':
         clint = ClientInformation()
         clint.clint_id = request.POST.get('clint_id')
         clint.name= request.POST.get('name')
         clint.phone= request.POST.get('phone')
         clint.address = request.POST.get('address')
         clint.save()
         return render(request,"dashboard/index.html")

def insert_mistri_information(request):
    if request.method == 'POST':
         mistri = MistriInformation()
         mistri.mistri_id = request.POST.get('mistri_id')
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
