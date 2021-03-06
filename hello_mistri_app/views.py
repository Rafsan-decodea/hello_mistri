
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
    mistri = MistriInformation.objects.all()
    client = ClientInformation.objects.all()
    context ={
        "mistri_data":mistri,
        "client_data":client,
    }
    return render(request,"index.html",context)

def dashboard(request):
     mistri = MistriInformation.objects.all()
     client = ClientInformation.objects.all()
     city  = City.objects.all()
     area =  Area.objects.all()
     sub_area = SubArea.objects.all()

     context = {
        "mistri_data":mistri,
        "client_data":client,
        "city":city,
        "area":area,
        "sub_area":sub_area,
       }

     return render(request ,"dashboard/personal_information.html",context)



def information(request):
    #{{user.social_auth.get.provider}} {{ user.social_auth.get.uid }}
    mistri = MistriInformation.objects.all()
    client = ClientInformation.objects.all()
    city  = City.objects.all()

    # get_cityid = request.POST.get("id")
    # if get_cityid != None:
    #   a = City.objects.get(pk=get_cityid)

    #   area = []
    #   area_id=[]
    #   for data in a.area_set.all():
    #       area.append(data.area_name)
    #       area_id.append(data.id)
    #   fetch_area = zip(area,area_id)
    #   print (fetch_area)
    # if get_cityid == None:
    #     fetch_area = zip("asdasd","aasdsad")


    # c = City.objects.get(pk=1)
    # for a in c.area_set.all():
    #     print ("Area is ====>",a.area_name)


    service = Service.objects.all()
    sub_service = SubService.objects.all()
    service_type = ServiceType.objects.all()
    # user = User.objects.get(id=request.user.id)
    # mistri = user.mistriinformation_set.all()
    # client = user.clientinformation_set.all()
    context ={
        "mistri_data":mistri,
        "client_data":client,
        "city":city,
        "service":service,
        "sub_service":sub_service,
        "service_type":service_type,
    }
    return render(request,"information.html",context)


def get_cityinformation(request):

     if request.is_ajax():

       get_cityid = request.POST.get("id")
       getcity = City.objects.get(pk=get_cityid)

       area = []
       area_id = []

       for data in getcity.area_set.all():
           area.append(data.area_name)
           area_id.append(data.id)

       get_area = list(zip(area,area_id))


       return response.JsonResponse({
             'msg' :'Success',
             'fetch_area':get_area,
        })


def get_areainformation(request):

     if request.is_ajax():
        get_area_id = request.POST.get("id")
        getarea = Area.objects.get(pk=get_area_id)

        subarea = []
        subarea_id = []

        for data in getarea.subarea_set.all():
             subarea.append(data.sub_area_name)
             subarea_id.append(data.id)
        print (subarea)
        get_subarea = list(zip(subarea,subarea_id))

        return response.JsonResponse({
             'msg' :'Success',
             'fetch_subarea':get_subarea,
        })


def insert_clint_information(request):

    if request.method == 'POST':
         u = User.objects.get(pk=request.user.id)# get Authenticate id and insert data to it
         clint_id = 1
         uid  = request.POST.get('client_uid')
         email = request.POST.get('client_email')
         profile_image_link = request.POST.get('client_profile_image_link')
         name= request.POST.get('name')
         phone= request.POST.get('number')
         city = request.POST.get('city_client')
         area = request.POST.get('area_client')
         sub_area = request.POST.get('sub_area_client')
         home_address = request.POST.get('home_address')
         c = ClientInformation.objects.create(user=u ,uid=uid ,email=email,profile_image_link=profile_image_link,clint_id=clint_id,name=name,phone=phone,city=city,area=area,sub_area=sub_area,home_address=home_address)
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
       c_data.home_address = request.POST.get('address')
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
         dob = request.POST.get('dob')
         city = request.POST.get('city')
         area = request.POST.get('area')
         sub_area = request.POST.get('sub_area')
         address = request.POST.get('address')

         ability = request.POST.get('ability')
         expiriance = request.POST.get('expiriance')
         emargency = request.POST.get('emargency')
         emargency_name = request.POST.get('emargency_name')
         emargency_number = request.POST.get('emargency_number')
         education = request.POST.get('education')
         is_bick = request.POST.get('is_bike')
         is_instrument = request.POST.get('is_instrument')
         service = request.POST.getlist('service')
         sub_service = request.POST.getlist('sub_service')
         service_type = request.POST.getlist('service_type')

         helper_mistri = request.POST.get('helper_mistri')


         MistriInformation.objects.create(user=u,mistri_id=mistri_id,uid=uid,email=email,profile_image_link=profile_image_link, name=name,phone=phone,image=image,dob=dob,city=city,area=area,sub_area=sub_area,address=address,ability=ability,expiriance=expiriance,emargency=emargency,emargency_name=emargency_name,emargency_number=emargency_number,education=education,is_bick=is_bick,is_instrument=is_instrument,service=service,sub_service=sub_service,service_type=service_type, helper_mistri=helper_mistri).save()
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
        #   m_data.address = request.POST.get('address')
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




def show_area(request):
    city  = City.objects.all()
    area =  Area.objects.all()
    sub_area = SubArea.objects.all()
    context = {
        "city":city,
        "area" :area,
        "sub_area":sub_area,

    }
    return render(request,"dashboard/admin/add_area.html",context)

def fetch_area(request):
    if request.is_ajax():
        city_id = request.POST.get("id")
        get_city = City.objects.get(pk=city_id)
        area=[]
        area_id =[]
        for data in get_city.area_set.all():
             area.append(data.area_name)
             area_id.append(data.id)
        fetch_area = list(zip(area,area_id))
        return response.JsonResponse({
             'msg' :'Success',
             'fetch_area':fetch_area,
           })

def fetch_subarea(request):
    if request.is_ajax():
        area_id = request.POST.get("id")
        get_area = Area.objects.get(pk=area_id)
        subarea = []
        subarea_id =[]
        for data in get_area.subarea_set.all():
            subarea.append(data.sub_area_name)
            subarea_id.append(data.id)
        fetch_subarea = list(zip(subarea,subarea_id))
        return response.JsonResponse({
             'msg' :'Success',
             'fetch_subarea':fetch_subarea,
           })

def delete_city(request):
    if request.is_ajax():
        city_id = request.POST.get("id")
        get_city = City.objects.get(pk=city_id)
        get_city.delete()
        return response.JsonResponse({
             'msg' :'Success',

           })

def delete_area(request):
    if request.is_ajax():
         area_id = request.POST.get("id")
         get_area = Area.objects.get(pk=area_id)
         get_area.delete()
         return response.JsonResponse({
             'msg' :'Success',

           })

def delete_subarea(request):
    if request.is_ajax():
         subarea_id = request.POST.get("id")
         get_subarea = SubArea.objects.get(pk=subarea_id)
         get_subarea.delete()
         return response.JsonResponse({
             'msg' :'Success',

           })

def  edit_city(request):
    if request.is_ajax():
         city_id = request.POST.get("id")
         city_get = City.objects.get(pk=city_id)
         city_get.city_name = request.POST.get("edit_city_name")
         city_get.save()
         return response.JsonResponse({
             'msg' :'Success',

           })

def edit_area(request):
    if request.is_ajax():
         city_id  = request.POST.get("get_cityid")
         city_get = City.objects.get(pk=city_id)
         area_id = request.POST.get("id")
         get_area = Area.objects.get(pk=area_id)
         get_area.city_name = city_get
         get_area.area_name = request.POST.get("edit_area_name")
         get_area.save()
         return response.JsonResponse({
             'msg' :'Success',

           })

def edit_subarea(request):
    if request.is_ajax():
         area_id = request.POST.get("get_areaid")
         area_get = Area.objects.get(pk=area_id)
         subarea_id =  request.POST.get("id")
         subarea_get = SubArea.objects.get(pk=subarea_id)
         subarea_get.area_name = area_get
         subarea_get.sub_area_name = request.POST.get("edit_subarea_name")
         subarea_get.save()
         return response.JsonResponse({
             'msg' :'Success',

           })


def add_city(request):
    if request.is_ajax():
       city = City.objects.all()
       city_name =  request.POST.get("city")
       print(request.POST.get("city"))
       City.objects.create(city_name=city_name).save()
    return response.JsonResponse({
             'msg' :'Success',
           })



def add_area(request):
    if request.is_ajax():
           city_id1 = request.POST.get("city_id")
           print ("====>",city_id1)
           city_name1 = City.objects.get(pk=city_id1)
           area_name = request.POST.get("area")
           print ("====>",area_name)
           Area.objects.create(city_name=city_name1,area_name=area_name).save()
    return response.JsonResponse({
             'msg' :'Success',
            })


def add_subarea(request):
      if request.is_ajax():
          area_id= request.POST.get("sub_area_id")
          area_name = Area.objects.get(pk=area_id)
          subarea_name = request.POST.get("subarea")
          SubArea.objects.create(area_name=area_name,sub_area_name=subarea_name).save()
      return response.JsonResponse({
             'msg' :'Success',
            })




#-------------- Service Segment ------------------------------


def show_service(request):
    service = Service.objects.all()
    sub_service = SubService.objects.all()
    service_type = ServiceType.objects.all()

    context = {
        "service":service,
        "sub_service":sub_service,
        "service_type":service_type,
    }
    return render(request,"dashboard/admin/add_service.html",context)



def add_service(request):
    if request.is_ajax():
        get_service = request.POST.get("service")
        Service.objects.create( service_name=get_service).save()
        return response.JsonResponse({
             'msg' :'Success',
            })
    return response.JsonResponse({
             'msg' :'error',
            })

def fetch_subservice(request):

    if request.is_ajax():
          service_id = request.POST.get("id")
          get_service = Service.objects.get(pk=service_id)
          sub_service= []
          sub_serviceid =[]

          for data in get_service.subservice_set.all():
              sub_service.append(data.sub_service_name)
              sub_serviceid.append(data.id)
          get_subservice = list(zip(sub_service,sub_serviceid))

          return response.JsonResponse({
             'msg' :'Success',
             'fetch_subservice':get_subservice,
            })


def fetch_servicetype(request):
    if request.is_ajax():
        servicetype_id = request.POST.get("id")
        get_subservice = SubService.objects.get(pk=servicetype_id)
        subservice = []
        subservice_rate= []
        subservice_id = []


        for data in get_subservice.servicetype_set.all():
              subservice.append(data.service_type)
              subservice_id.append(data.id)
              subservice_rate.append(data.service_type_rate)
        get_servicetype = list(zip(subservice,subservice_id,subservice_rate))

        return response.JsonResponse({
             'msg' :'Success',
             'fetch_servicetype':get_servicetype,
            })



def add_subservice(request):
     if request.is_ajax():
         service_id = request.POST.get("service_id")
         print (service_id)
         service_get = Service.objects.get(pk=service_id)
         sub_service = request.POST.get("sub_service")
         SubService.objects.create(service_name=service_get,sub_service_name=sub_service).save()
         return response.JsonResponse({
             'msg' :'Success',
            })
     return response.JsonResponse({
             'msg' :'error',
            })



def add_servicetype(request):
     if request.is_ajax():
         sub_service_id = request.POST.get("subservice_id")
         subservice_get = SubService.objects.get(pk=sub_service_id)
         service_type = request.POST.get("service_type")
         service_type_amount = request.POST.get("service_type_amount")
         ServiceType.objects.create(service_name=subservice_get,service_type=service_type, service_type_rate=service_type_amount).save()

         return response.JsonResponse({
             'msg' :'Success',
            })
     return response.JsonResponse({
             'msg' :'error',
            })


def delete_service(request):
     if request.is_ajax():
        service_id = request.POST.get("id")
        service = Service.objects.get(pk=service_id)
        service.delete()
        return response.JsonResponse({
             'msg' :'Success',
            })

def edit_service(request):
    if request.is_ajax():

        service_id = request.POST.get("id")
        service =  Service.objects.get(pk=service_id)
        service.service_name = request.POST.get("change_name_service")
        service.save()
        return response.JsonResponse({
             'msg' :'Success',
            })


def edit_subservice(request):
    if request.is_ajax():
        service_id = request.POST.get("service_id")
        fetch_service = Service.objects.get(pk=service_id)
        subservice_id = request.POST.get("id")
        subservice =  SubService.objects.get(pk=subservice_id)
        subservice.service_name = fetch_service
        subservice.sub_service_name  = request.POST.get("change_name_subservice")

        subservice.save()
        return response.JsonResponse({
             'msg' :'Success',
            })


def edit_subservicetype(request):
      if request.is_ajax():
            subservice_id = request.POST.get("subservice_id")
            fetch_subservice = SubService.objects.get(pk=subservice_id)
            servicetype_id = request.POST.get("id")
            servicetype = ServiceType.objects.get(pk=servicetype_id)
            servicetype.service_name = fetch_subservice
            servicetype.service_type = request.POST.get("change_name_servicetype")
            servicetype.service_type_rate = request.POST.get("change_servicetype_rate")

            servicetype.save()
            return response.JsonResponse({
             'msg' :'Success',
            })




def delete_subservice(request):
    if request.is_ajax():
        sub_service_id = request.POST.get("id")
        subservice = SubService.objects.get(pk=sub_service_id)
        subservice.delete()
        return response.JsonResponse({
             'msg' :'Success',
            })

def delete_subservicetype(request):
    if request.is_ajax():
        sub_service_type = request.POST.get("id")
        subservicetype = ServiceType.objects.get(pk=sub_service_type)
        subservicetype.delete()
        return response.JsonResponse({
             'msg' :'Success',
            })



def client_order_recive(request):
      order = OrderSubmitByClient.objects.all()
      mistri =  MistriInformation.objects.all()

    #   mistri_name =[]
    #   mistri_services = []
    #   mistri_phone = []
    #   mistri_area =[]
    #   for x in mistri:
    #       mistri_service = x.service.strip("']").strip("['").replace("'","").split(",")
    #       for y in mistri_service:
    #             mistri_services.append(y.strip(" "))
    #       mistri_name.append(x.name)
    #       mistri_phone.append(x.phone)
    #       mistri_area.append(x.area)

    #   # There is a problem That not filter Area
    #   import itertools
    #   fill = mistri_area[-1] if (len(mistri_area) < len(mistri_name)) else mistri_name[-1]
    #   final_data = list(itertools.zip_longest(mistri_name,mistri_services, mistri_area,fillvalue=fill))
     
    # ------- Not Order by  mistri area ---------

      import collections
      services = collections.defaultdict(list)

      for data in mistri:
           for test in data.service.strip("']").strip("['").replace("'","").split(","):
             services[test.strip(" ")].append([data.name,data.phone,data.profile_image_link])  
     
      
      context = {
          "orders":order,
          "mistri":mistri,
        #   "mistri_information":final_data,   
          "mistri_services":dict(services),        
      }
      return render(request,"dashboard/admin/client_orderlist.html",context)

def client_order_process(request):
     if request.is_ajax():
          mistri_list  = request.POST.getlist("mistri_name_data")
          discount_amount = request.POST.get("discountAmount")
          print (mistri_list,"===>",discount_amount)

          return response.JsonResponse({
              'msg':'success',
              'mistri_list':list(mistri_list),
              'discount_amount':discount_amount,
          })

#------------------client Dashboard Part -------------------------

def client_service_select(request):
     mistri = MistriInformation.objects.all()
     client = ClientInformation.objects.all()
     service = Service.objects.all()

     context ={
         "mistri_data":mistri,
         "client_data":client,
         "service":service,
     }
     return render(request,"dashboard/client_service_select.html" ,context)



def submit_client_order(request):
   if request.is_ajax():
        user_get =  User.objects.get(pk=request.user.id)
        orderholder_name =  request.user.get_full_name()
        order_holder_pic =  request.POST.get("order_holder_pic")
        service_name = request.POST.get("service_name")
        subservice_name = request.POST.get("subservice_name")
        servicetype_name = request.POST.get("service_type")
        servicetype_rate = request.POST.get("service_type_rate")
        client_city = request.POST.get("client_city")
        client_area = request.POST.get("client_area")
        client_uid =  request.POST.get("client_uid")
        time = request.POST.get("time");
        status = request.POST.get("status")
        OrderSubmitByClient.objects.create(user=user_get, order_holder_name= orderholder_name,order_holder_pic= order_holder_pic,service_name=service_name,sub_service_name=subservice_name,service_type=servicetype_name,order_holder_city=client_city,order_holder_area=client_area,service_type_rate=servicetype_rate ,time=time,status=status,order_holder_uid=client_uid).save()
        return response.JsonResponse({
             'msg' :'Success',
            })


#---------------- Mistri Dashboard part --------------------

def mistri_painding_work(request):
     mistri = MistriInformation.objects.all()
     client = ClientInformation.objects.all()
     service = Service.objects.all()

     context ={
         "mistri_data":mistri,
         "client_data":client,
         "service":service,
     }
     return render(request,"dashboard/mistri_painding_work.html",context)



def logout(request):
    user_logout(request)
    return render(request,"index.html")
# Create your views here.
