from django.contrib import admin
from deployment.models import *


class HostNameAdmin(admin.ModelAdmin):
    list_display = ('label', 'dir_path', 'panel')
    list_filter = ['panel']


class PlatformAdmin(admin.ModelAdmin):
    list_display = ('label', 'panel')
    list_filter = ['panel']


class ChannelAdmin(admin.ModelAdmin):
    list_display = ('label', 'panel')
    list_filter = ['panel']


class IpAdmin(admin.ModelAdmin):
    list_display = ('label', 'panel')
    list_filter = ['panel']


class CIWPAdmin(admin.ModelAdmin):
    list_display = ('label', 'panel')
    list_filter = ['panel']


class ProcessServerAdmin(admin.ModelAdmin):
    list_display = ('label', 'panel')
    list_filter = ['panel']


class UpLoadworkOrderAdmin(admin.ModelAdmin):
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


class UpLoadworkOrderLockAdmin(admin.ModelAdmin):
    list_display = ('hpc', 'status_label', 'panel')
    list_filter = ['panel', 'hostname', 'platform', 'channel']

    def hpc(self, obj):
        return '{0}/{1}/{2}'.format(obj.hostname, obj.platform, obj.channel)

    def status_label(self, obj):
        if obj.status == 0:
            return 'UNLOCK'
        else:
            return 'LOCKING'


class ServerControlWorkOrderAdmin(admin.ModelAdmin):
    list_display = (
        'server',
        'panel',
        'parameter',
        'date',
        'progress',
        'result',
        'user')
    list_filter = ['panel', 'server']

    def parameter(self, obj):
        return '{0}/{1}/{2}/{3}/{4}'.format(
            obj.parameter1,
            obj.parameter2,
            obj.parameter3,
            obj.parameter4,
            obj.parameter5)

    def date(self, obj):
        return '{0} - {1}'.format(obj.start_date, obj.stop_date)


class ServerControlWorkOrderLockAdmin(admin.ModelAdmin):
    list_display = ('server', 'status_label', 'panel')
    list_filter = ['panel', 'server']

    def status_label(self, obj):
        if obj.status == 0:
            return 'UNLOCK'
        else:
            return 'LOCKING'


class ServerConfigOrderAdmin(admin.ModelAdmin):
    list_display = (
        'panel',
        'ciwp',
        'version',
        'db_filename',
        'ps_filename',
        'hs_filename',
        'date',
        'user')
    list_filter = ['panel']

admin.site.register(HostName, HostNameAdmin)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(Channel, ChannelAdmin)
admin.site.register(Ip, IpAdmin)
admin.site.register(CIWP, CIWPAdmin)
admin.site.register(ProcessServer, ProcessServerAdmin)
admin.site.register(UpLoadWorkOrder, UpLoadworkOrderAdmin)
admin.site.register(UpLoadWorkOrderLock, UpLoadworkOrderLockAdmin)
admin.site.register(ServerControlWorkOrder, ServerControlWorkOrderAdmin)
admin.site.register(ServerControlWorkOrderLock, ServerControlWorkOrderLockAdmin)
admin.site.register(ServerConfigOrder, ServerConfigOrderAdmin)
