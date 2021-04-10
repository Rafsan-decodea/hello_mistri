from __future__ import unicode_literals
from django.db import models
from django.db.models.fields.files import ImageField
from phone_field import PhoneField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.






class ClientInformation(models.Model):  
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   clint_id = models.IntegerField()
   name = models.CharField(max_length=100)
   phone = PhoneField(blank=False, help_text='Contact phone number')
   address = models.CharField(max_length=500)



   def __str__(self):
            return 'Clint Name ==> {0}'.format(self.name)


class Admin(models.Model):
       id = models.AutoField(primary_key=True)
       admin_id = models.IntegerField()
       name = models.CharField(max_length=100)
       def __str__(self):
            return 'Admin Name ==> {0}'.format(self.name)





class MistriInformation(models.Model):
       user = models.ForeignKey(User, on_delete=models.CASCADE)
       mistri_id = models.IntegerField()
       name = models.CharField(max_length=100)
       phone = PhoneField(blank=False,help_text='Contact phone number')
       image = models.ImageField(upload_to='media')
       dob = models.CharField(max_length=500)
       address =models.CharField(max_length=500)
 
       def __str__(self):
              return 'Mistri name ==>{0}'.format(self.name)




# class Mistri_UID(models.Model):
#       mistri = models.OneToOneField(MistriInformation,on_delete=models.CASCADE,primary_key=True)
#       uid = models.CharField(max_length=1000)

# class Clint_UID(models.Model):
#       clint = models.OneToOneField(ClientInformation,on_delete=models.CASCADE,primary_key=True)
#       uid = models.CharField(max_length=1000)





# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         ClientInformation.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.clientinformation.save()