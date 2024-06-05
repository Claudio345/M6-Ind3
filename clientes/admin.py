from django.contrib import admin
from . models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'image','nombre','correo')
    
admin.site.register(Cliente, ClienteAdmin)