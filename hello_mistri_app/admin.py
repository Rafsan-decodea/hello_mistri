from django.contrib import admin
from .models import *

admin.site.register(ClientInformation)
admin.site.register(MistriInformation)
admin.site.register(City)
admin.site.register(Area)
admin.site.register(SubArea)


admin.site.register(Service)
admin.site.register(SubService)
admin.site.register(ServiceType)

admin.site.register(OrderSubmitByClient)

# admin.site.register(Admin)
# admin.site.register(Mistri_UID)
# admin.site.register(Clint_UID)


