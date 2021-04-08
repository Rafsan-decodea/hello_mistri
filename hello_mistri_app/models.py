from django.db import models
from django.db.models.fields.files import ImageField
from phone_field import PhoneField

# Create your models here.


class ClientInformation(models.Model):  
   id = models.AutoField(primary_key=True)
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
       id = models.AutoField(primary_key=True)
       mistri_id = models.IntegerField()
       name = models.CharField(max_length=100)
       phone = PhoneField(blank=False,help_text='Contact phone number')
       image = models.ImageField(upload_to='media')
       dob = models.CharField(max_length=500)
       address =models.CharField(max_length=500)

       def __str__(self):
              return 'Mistri name ==>{0}'.format(self.name)

       
