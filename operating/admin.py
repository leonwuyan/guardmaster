from django.contrib import admin
from operating.models import Server

# Register your models here.


class ServerAdmin(admin.ModelAdmin):
    list_display = ('label', 'panel', 'ip', 'port', 'hostname', 'home')
    search_fields = ['label']
    list_filter = ['panel']

admin.site.register(Server, ServerAdmin)
