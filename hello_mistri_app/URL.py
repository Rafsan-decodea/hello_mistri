from django.conf.urls import url
from django.urls.conf import path
from . import views

urlpatterns = [
     path(r'',views.index ,name="home" ),
     path(r'dashboard',views.dashboard, name="dashboard"),
     path(r'information',views.information, name="information"),
     path(r'insert_client',views.insert_clint_information, name="insert_client"),
     path(r'update_client',views.update_client_information,name="update_client"),
     path(r'insert_mistri',views.insert_mistri_information,name="insert_mistri"),
     path(r'update_mistri',views.update_mistri_information,name="update_mistri"),

     path(r'admin_login',views.admin_login_page,name="admin_login"),
     path(r'admin_dashboard',views.admin_dashboard,name="admin_dashboard"),
     path(r'see_mistri',views.see_mistri, name="see_mistri"),
     path(r'see_client',views.see_client,name="see_client"),

     path(r'show_area',views.show_area,name="show_area"), 
     path(r'add_city',views.add_city,name="add_city"),
     path(r'add_area',views.add_area,name="add_area"),
     path(r'add_sub_area',views.add_subarea,name="add_sub_area"),

     path(r'add_service',views.add_service,name="add_service"),
     path(r'add_subservice',views.add_subservice,name="add_subservice"),
     path('add_servicetype',views.add_servicetype,name="add_servicetype"),
     path(r'show_service',views.show_service,name="show_service"),
     
     #--------------------Fetch information Segment ------------------------
     path(r'get_cityinformation',views.get_cityinformation,name="get_cityinformation"),
     path(r'get_areainformation',views.get_areainformation,name="get_areainformation"),
     
     path(r'login',views.login,name="login"),
     path(r'logout', views.logout, name="logout"),
     
]