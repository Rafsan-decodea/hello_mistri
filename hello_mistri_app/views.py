from django.http import response
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import backends, logout as user_logout
from .models import *


def index(request):
    return render(request,"index.html")

def dashboard(request): 
     admin = Admin.objects.all()
     mistri = MistriInformation.objects.all()
     client = ClientInformation.objects.all()

     context = {
        "admin" : admin,
        "mistri_data":mistri,
        "client_data":client,
       }
   
     return render(request ,"dashboard/personal_information.html",context)




def information(request):
    #{{user.social_auth.get.provider}} {{ user.social_auth.get.uid }}
    mistri = MistriInformation.objects.all()
    client = ClientInformation.objects.all()
    # user = User.objects.get(id=request.user.id)
    # mistri = user.mistriinformation_set.all()
    # client = user.clientinformation_set.all()
    context ={
        "mistri_data":mistri,
        "client_data":client,
    }
    return render(request,"information.html",context)

def insert_clint_information(request):
    
    if request.method == 'POST':
         u = User.objects.get(pk=request.user.id)# get Authenticate id and insert data to it
         clint_id = request.POST.get('clint_id') 
         uid  = request.POST.get('client_uid')
         name= request.POST.get('name')
         phone= request.POST.get('phone')
         address = request.POST.get('address')
         c = ClientInformation.objects.create(user=u ,uid=uid ,clint_id=clint_id,name=name,phone=phone,address=address)
         c.save()     
        
    return render(request,"dashboard/personal_information.html")

def insert_mistri_information(request):
    if request.method == 'POST':
         u = User.objects.get(pk=request.user.id)
         mistri_id = request.POST.get('mistri_id')
         uid = request.POST.get('mistri_uid')
         name = request.POST.get('name')
         phone = request.POST.get('number')
         image = request.FILES['image']  
         address = request.POST.get('address')
         dob = request.POST.get('dob')
         MistriInformation.objects.create(user=u,mistri_id=mistri_id,uid=uid,name=name,phone=phone,image=image,address=address,dob=dob).save()
    return render(request,"dashboard/personal_information.html")

def update_mistri_information(request):
    if  request.method == 'POST':
          u = User.objects.get(pk=request.user.id)
          m = MistriInformation.objects.all()
          global mid
          for x in  m:
               mid = x.id
          m_data = MistriInformation.objects.get(pk=mid)
          m_data.mistri_id = request.POST.get('mistri_id')
          m_data.uid = request.POST.get('mistri_uid')
          m_data.name = request.POST.get('name')
          m_data.phone = request.POST.get('number')
          try:
             m_data.image = request.FILES['image'] 
          except :
              pass
          m_data.address = request.POST.get('address')
          m_data.dob = request.POST.get('dob') 
#user=u,mistri_id=mistri_id,uid=uid,name=name,phone=phone,image=image,address=address,dob=dob
          m_data.save()
    return render(request,"dashboard/personal_information.html")



def logout(request):
    user_logout(request)
    return render(request,"index.html")
# Create your views here.
