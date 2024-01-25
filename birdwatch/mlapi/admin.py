from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Birds) 
admin.site.register(BirdsStatus)
admin.site.register(BirdsDetail)
admin.site.register(NodeDevice)