from __future__ import unicode_literals
from django.db import models
from django.db.models.fields.files import ImageField
from phone_field import PhoneField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.






class ClientInformation(models.Model):  
   user = models.OneToOneField(User, on_delete=models.CASCADE ) # Relation With one to one User Model
   clint_id = models.CharField(max_length=10)
   uid = models.CharField(max_length=1000)
   email = models.CharField(max_length=100)
   profile_image_link = models.CharField(max_length=400)
   name = models.CharField(max_length=100)
   phone = PhoneField(blank=False, help_text='Contact phone number')
   address = models.CharField(max_length=500)
   city= models.CharField(max_length=100)
   area = models.CharField(max_length=200)
   sub_area =models.CharField(max_length=200)


   
   def __str__(self):
            return 'Clint Name ==> {0}'.format(self.name)
    








class MistriInformation(models.Model):
       user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)# Relation With one to one User Model And True Nullable
       mistri_id = models.CharField(max_length=10)
       uid = models.CharField(max_length=1000)
       email = models.CharField(max_length=100)
       profile_image_link = models.CharField(max_length=400)
       name = models.CharField(max_length=100)
       phone = PhoneField(blank=False,help_text='Contact phone number')
       image = models.ImageField(upload_to='media')
       dob = models.CharField(max_length=500)
       city= models.CharField(max_length=100)
       area = models.CharField(max_length=200)
       sub_area =models.CharField(max_length=200)
       address = models.CharField(max_length=200)
       




 
       def __str__(self):
              return 'Mistri name ==>{0}'.format(self.name)




class City(models.Model):
       city_name = models.CharField(max_length=100)
       def __str__(self):
              return 'City name ==>{0}'.format(self.city_name)

class Area(models.Model):
       city_name =  models.ForeignKey(City, on_delete=models.CASCADE)
       area_name = models.CharField(max_length=100)
       sub_area_name = models.CharField(max_length=100)
       def __str__(self):
              return 'Area name ==>{0} {1}'.format(self.area_name,self.sub_area_name)



class Service(models.Model):
       service_name = models.CharField(max_length=100)
       def __str__(self):
              return 'Service name ==>{0}'.format(self.service_name)

class SubService(models.Model):
       service_name =  models.ForeignKey(Service, on_delete=models.CASCADE)
       sub_service_name = models.CharField(max_length=100)

       def __str__(self):
              return 'Sub Service name ==>{0}'.format(self.sub_service_name)



class MainWork(models.Model):
       main_work_name = models.CharField(max_length=100)
       def __str__(self):
              return 'Main Work ==>{0}'.format(self.main_work)
       
class SubWork(models.Model):
       main_work = models.ForeignKey(MainWork, on_delete=models.CASCADE)
       sub_work_name =  models.CharField(max_length=100)