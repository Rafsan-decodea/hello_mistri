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
     path(r'login',views.login,name="login"),
     path(r'logout', views.logout, name="logout"),
     
]