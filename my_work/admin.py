from django.contrib import admin
from .models import User,GarbageBin,Complaint,UserGarbageBin,Area,UserArea
# Register your models here.
admin.site.register(User)
admin.site.register(GarbageBin)
admin.site.register(Complaint)
admin.site.register(UserGarbageBin)
admin.site.register(Area)
admin.site.register(UserArea)
