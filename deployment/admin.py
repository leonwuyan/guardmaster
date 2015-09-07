from django.contrib import admin
from deployment.models import HostName, Platform, Channel, UpLoadWorkOrder, UpLoadWorkOrderLock


class UIHostNameAdmin(admin.ModelAdmin):
    list_display = ('label', 'dir_path', 'panel')
    list_filter = ['panel']


class UIPlatformAdmin(admin.ModelAdmin):
    list_display = ('label', 'panel')
    list_filter = ['panel']


class UIChannelAdmin(admin.ModelAdmin):
    list_display = ('label', 'panel')
    list_filter = ['panel']


class UIUpLoadworkOrderAdmin(admin.ModelAdmin):
    list_display = (
        'version',
        'panel',
        'hpc',
        'date',
        'progress',
        'result',
        'user')
    list_filter = ['panel', 'hostname', 'platform', 'channel', 'version']

    def hpc(self, obj):
        return '{0}/{1}/{2}'.format(obj.hostname, obj.platform, obj.channel)

    def date(self, obj):
        return '{0} - {1}'.format(obj.start_date, obj.stop_date)


class UIUpLoadworkOrderLockAdmin(admin.ModelAdmin):
    list_display = ('hpc', 'status_label', 'panel')
    list_filter = ['panel', 'hostname', 'platform', 'channel']

    def hpc(self, obj):
        return '{0}/{1}/{2}'.format(obj.hostname, obj.platform, obj.channel)

    def status_label(self, obj):
        if obj.status == 0:
            return 'UNLOCK'
        else:
            return 'LOCKING'

admin.site.register(HostName, UIHostNameAdmin)
admin.site.register(Platform, UIPlatformAdmin)
admin.site.register(Channel, UIChannelAdmin)
admin.site.register(UpLoadWorkOrder, UIUpLoadworkOrderAdmin)
admin.site.register(UpLoadWorkOrderLock, UIUpLoadworkOrderLockAdmin)
