from django.contrib import admin
from operating.models import Server, ResponseMail, Notify

# Register your models here.


class ServerAdmin(admin.ModelAdmin):
    list_display = ('label', 'panel', 'server_type', 'ip', 'hostname')
    search_fields = ['label']
    list_filter = ['panel', 'server_type']


class ResponseMailAdmin(admin.ModelAdmin):
    list_display = ('server', 'title', 'uid', 'guardmaster', 'pub_date')
    search_fields = ['title']
    list_filter = ['server']


class NotifyAdmin(admin.ModelAdmin):
    list_display = ('title', 'panel', 'notify_url', 'hostname', 'channel', 'world_id', 'seqid')
    search_fields = ['title']
    list_filter = ['panel', 'hostname', 'channel', 'platform', 'world_id']

admin.site.register(Server, ServerAdmin)
admin.site.register(ResponseMail, ResponseMailAdmin)
admin.site.register(Notify, NotifyAdmin)
