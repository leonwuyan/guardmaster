from django.contrib import admin
from operating.models import Server, ResponseMail, CDNServer, Notify

# Register your models here.


class ServerAdmin(admin.ModelAdmin):
    list_display = ('label', 'panel', 'ip', 'port', 'hostname', 'home')
    search_fields = ['label']
    list_filter = ['panel']


class CDNServerAdmin(admin.ModelAdmin):
    list_display = ('label', 'panel', 'ip', 'port', 'hostname', 'home', 'cdn_url')
    search_fields = ['label']
    list_filter = ['panel']


class ResponseMailAdmin(admin.ModelAdmin):
    list_display = ('server', 'title', 'uid', 'guardmaster', 'pub_date')
    search_fields = ['title']
    list_filter = ['server']


class NotifyAdmin(admin.ModelAdmin):
    list_display = ('title', 'panel', 'notify_url', 'hostname', 'channel', 'world_id', 'seqid')
    search_fields = ['title']
    list_filter = ['panel', 'hostname', 'channel', 'platform', 'world_id']

admin.site.register(Server, ServerAdmin)
admin.site.register(CDNServer, CDNServerAdmin)
admin.site.register(ResponseMail, ResponseMailAdmin)
admin.site.register(Notify, NotifyAdmin)
