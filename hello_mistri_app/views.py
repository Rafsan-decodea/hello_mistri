from django.http import response
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import backends, logout as user_logout



def index(request):
    return render(request,"index.html")

def dashboard(request): 
    return render(request ,"dashboard/index.html")

def logout(request):
    user_logout(request)
    return render(request,"index.html")
# Create your views here.
