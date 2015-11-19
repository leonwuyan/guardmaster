from django.contrib import admin
from operating.models import Server, ResponseMail, Notify, ResponseAllMail

# Register your models here.


class ServerAdmin(admin.ModelAdmin):
    list_display = ('label', 'panel', 'server_type', 'ip', 'inetip', 'hostname')
    search_fields = ['label']
    list_filter = ['panel', 'server_type']


class ResponseMailAdmin(admin.ModelAdmin):
    list_display = ('server', 'title', 'uid', 'guardmaster', 'pub_date')
    search_fields = ['title']
    list_filter = ['server']


class ResponseAllMailAdmin(admin.ModelAdmin):
    list_display = ('server', 'title', 'zone', 'guardmaster', 'version', 'start_date', 'end_date')
    search_fields = ['title']
    list_filter = ['server']


class NotifyAdmin(admin.ModelAdmin):
    list_display = ('title', 'panel', 'hostname', 'channel', 'image_width', 'image_height', 'world_id', 'is_title', 'seqid')
    search_fields = ['title']
    list_filter = ['panel', 'hostname', 'channel', 'platform', 'world_id']

admin.site.register(Server, ServerAdmin)
admin.site.register(ResponseMail, ResponseMailAdmin)
admin.site.register(ResponseAllMail, ResponseAllMailAdmin)
admin.site.register(Notify, NotifyAdmin)
