from django.http import response
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import backends, logout as user_logout
from .models import *
# from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import *
from django.urls import reverse


def index(request):
    return render(request,"index.html")

def dashboard(request): 
     mistri = MistriInformation.objects.all()
     client = ClientInformation.objects.all()

     context = {
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
         clint_id = 1
         uid  = request.POST.get('client_uid')
         email = request.POST.get('client_email')
         profile_image_link = request.POST.get('client_profile_image_link')
         name= request.POST.get('name')
         phone= request.POST.get('phone')
         address = request.POST.get('address')
         c = ClientInformation.objects.create(user=u ,uid=uid ,email=email,profile_image_link=profile_image_link,clint_id=clint_id,name=name,phone=phone,address=address)
         c.save()     
        
    return render(request,"dashboard/personal_information.html")

# @ensure_csrf_cookie
def update_client_information(request):
    if request.is_ajax(): 
       u = User.objects.get(pk=request.user.id)
       c = ClientInformation.objects.all()
       global cid
       global cuid
       global memail
       for x in c:
           cid = x.id   
           cuid =x.uid
           cemail =x.email
           cplink = x.profile_image_link
       c_data = ClientInformation.objects.get(pk=cid)  
       c_data.clint_id = 1 
       c_data.uid =  cuid
       c_data.email = cemail
       c_data.profile_image_link = cplink
       c_data.name = request.POST.get('name')
       c_data.phone =request.POST.get('phone')
       c_data.address = request.POST.get('address')
       c_data.save() 
    # return render(request,"dashboard/personal_information.html")
       return response.JsonResponse({
             'msg' :'Success',
      })

def insert_mistri_information(request):
     if  request.method == 'POST':
         u = User.objects.get(pk=request.user.id)
         mistri_id = 2
         uid = request.POST.get('mistri_uid')
         email = request.POST.get('mistri_email')
         profile_image_link = request.POST.get('mistri_profile_image_link')
         name = request.POST.get('name')
         phone = request.POST.get('number')
         image = request.FILES['image']  
         address = request.POST.get('address')
         dob = request.POST.get('dob')
         MistriInformation.objects.create(user=u,mistri_id=mistri_id,uid=uid,email=email,profile_image_link=profile_image_link, name=name,phone=phone,image=image,address=address,dob=dob).save()
     return render(request,"dashboard/personal_information.html")


@csrf_exempt
def update_mistri_information(request):
       if request.is_ajax():
          u = User.objects.get(pk=request.user.id)
          m = MistriInformation.objects.all()
          global mid
          global muid
          global memail
          global mplink
          for x in  m:
               mid = x.id
               muid =x.uid
               memail = x.email
               mplink = x.profile_image_link
          m_data = MistriInformation.objects.get(pk=mid)
          m_data.mistri_id = 2
          m_data.uid = muid
          m_data.email = memail
          m_data.profile_image_link = mplink
          m_data.name = request.POST.get('name')
          m_data.phone = request.POST.get('number')
          try:
             m_data.image = request.FILES['image'] 
             print (request.FILES['image'])
             print ("fuck From image")
          except :
              print ("fuck without  image")
          m_data.address = request.POST.get('address')
          m_data.dob = request.POST.get('dob') 
         
#user=u,mistri_id=mistri_id,uid=uid,name=name,phone=phone,image=image,address=address,dob=dob
          m_data.save()
       return response.JsonResponse({
             'msg' :'Success',
      })


def admin_dashboard(request): 
    return render(request, "dashboard/admin/dashboard.html")

def admin_login_page(request): 
    return render(request,"dashboard/admin/login.html")

def login(request):
    
    if request.method == "POST":
         context = {}
         username = request.POST.get("username")
         password = request.POST.get("password")
         user = authenticate(request, username=username ,password=password)
         if user:
             auth.login(request,user)
             return HttpResponseRedirect(reverse("admin_dashboard"))
         else:
             return render(request, 'dashboard/admin/login.html',{'error':'User name or password not matching'})
    return render(request,"dashboard/admin/login.html")



def see_mistri(request):
    mistri = MistriInformation.objects.all()
    context = {
        "mistri_data":mistri,
    }
    return render(request,"dashboard/admin/see_mistri.html",context )

def see_client(request):
     client = ClientInformation.objects.all()
     context = {
         "client_data":client,
     }
     return render(request,"dashboard/admin/see_client.html",context )

def add_area(request):
    city  = City.objects.all()
    area = Area.objects.all()
    sub_area = SubArea.objects.all()
    context = {
        "city":city,
        "area":area,
        "sub_area":sub_area,
    }
    return render(request,"dashboard/admin/add_area.html",context)



def add_area_request(request):
    if request.is_ajax():
       city = City.objects.all()
    #    area = Area.objects.all()
    #    sub_area = SubArea.objects.all()
       city_name =  request.POST.get("city")
       print(request.POST.get("city"))
       city.create(city_name=city_name).save()
    #    for x in city:
    #        if x.city_name == city_name:
    #             return response.JsonResponse({
    #              'msg' :'city',
    #           })
    #        else:
    #           city.create(city_name=city_name).save()
      
      
       try:
           global cityid
           for x in city:
               cityid = x.id
           getcity = City.objects.get(pk=cityid)
           area_name = request.POST.get("area")
           Area.objects.create(city_name=getcity,area_name=area_name).save()
       except:
              print ("not Trigger Area")
        
       try:
            global areaid
            for x in Area.objects.all():
                 areaid = x.id
            getarea = Area.objects.get(pk=areaid)
            subarea_name = request.POST.get("subarea")
            SubArea.objects.create(area_name=getarea, sub_area_name=subarea_name).save()
       except :
            print ("not Trigger Sub area")
       
       return response.JsonResponse({
             'msg' :'Success',
      })




        





def logout(request):
    user_logout(request)
    return render(request,"index.html")
# Create your views here.
