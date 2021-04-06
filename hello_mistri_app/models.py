from django.db import models
from phone_field import PhoneField

# Create your models here.


class Client(models.Model):  
   id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=100)
   phone = PhoneField(blank=False, help_text='Contact phone number')
   address = models.CharField(max_length=500)


   def __str__(self):
            return 'Clint Name ==> {0}'.format(self.name)

