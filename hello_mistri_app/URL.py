from django.conf.urls import url
from django.urls.conf import path
from . import views

urlpatterns = [
     path(r'',views.index ,name="home" ),
     path(r'dashboard',views.dashboard, name="dashboard"),
     path(r'information',views.information, name="information"),
     path(r'logout', views.logout, name="logout"),
     
]