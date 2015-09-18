from django.contrib import admin
from deployment.models import HostName, Platform, Channel, UpLoadWorkOrder, UpLoadWorkOrderLock, TplItem, TplTemplate


class HostNameAdmin(admin.ModelAdmin):
    list_display = ('label', 'dir_path', 'panel')
    list_filter = ['panel']


class PlatformAdmin(admin.ModelAdmin):
    list_display = ('label', 'panel')
    list_filter = ['panel']


class ChannelAdmin(admin.ModelAdmin):
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


class TplItemInline(admin.TabularInline):
    model = TplItem
    extra = 3


class TplItemAdmin(admin.ModelAdmin):
    list_display = ('tpl_template', 'module_name', 'module_times', 'item_name', 'seqid', 'module_seqid')
    list_filter = ['tpl_template', 'module_name']


class TplTemplateAdmin(admin.ModelAdmin):
    inlines = [TplItemInline]
    list_display = ('tpl_type', 'out_file_type', 'out_name_mask', 'out_dir', 'saved_path')

admin.site.register(HostName, HostNameAdmin)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(Channel, ChannelAdmin)
admin.site.register(UpLoadWorkOrder, UpLoadworkOrderAdmin)
admin.site.register(UpLoadWorkOrderLock, UpLoadworkOrderLockAdmin)
admin.site.register(TplItem, TplItemAdmin)
admin.site.register(TplTemplate, TplTemplateAdmin)
