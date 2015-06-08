from django.contrib import admin
from operating.models import Server, ResponseMail

# Register your models here.


class ServerAdmin(admin.ModelAdmin):
    list_display = ('label', 'panel', 'ip', 'port', 'hostname', 'home')
    search_fields = ['label']
    list_filter = ['panel']


class ResponseMailAdmin(admin.ModelAdmin):
    list_display = ('server', 'title', 'uid', 'guardmaster', 'pub_date')
    search_fields = ['title']
    list_filter = ['server']

admin.site.register(Server, ServerAdmin)
admin.site.register(ResponseMail, ResponseMailAdmin)
