from django.conf.urls import url
from django.urls.conf import path
from . import views

urlpatterns = [
     path(r'',views.index ,name="home" ),
     path(r'dashboard',views.dashboard, name="dashboard"),
     path(r'information',views.information, name="information"),
     path(r'insert_client',views.insert_clint_information, name="insert_client"),
     path(r'insert_mistri',views.insert_mistri_information,name="insert_mistri"),
     path(r'update_mistri',views.update_mistri_information,name="update_mistri"),
     path(r'logout', views.logout, name="logout"),
     
]