from django.contrib import admin
from detection.models import Excuse, Panel, UIColMap, UIMainMenu, UISubMenu
# Register your models here.


class UIColMapInline(admin.TabularInline):
    model = UIColMap
    extra = 3


class UISubMenuInline(admin.TabularInline):
    model = UISubMenu
    extra = 3


class UIColMapAdmin(admin.ModelAdmin):
    list_display = (
        'label',
        'sub_menu',
        'col_name',
        'col_type',
        'seqid')
    search_fields = ['label']


class UISubMenuAdmin(admin.ModelAdmin):
    inlines = [UIColMapInline]
    list_display = (
        'label',
        'main_menu',
        'url',
        'table_name',
        'category',
        'seqid')
    search_fields = ['label']


class UIMainMenuAdmin(admin.ModelAdmin):
    inlines = [UISubMenuInline]
    list_display = ('label', 'groups_list', 'seqid')
    search_fields = ['label']

    def groups_list(self, obj):
        groups = ""
        for group in obj.groups.all():
            groups += group.name + ' | '
        return groups


class PanelAdmin(admin.ModelAdmin):
    list_display = ('label', 'groups_list', 'db_aliases')
    search_fields = ['label']

    def groups_list(self, obj):
        groups = ""
        for group in obj.groups.all():
            groups += group.name + ' | '
        return groups

admin.site.register(Excuse)
admin.site.register(Panel, PanelAdmin)
admin.site.register(UIColMap, UIColMapAdmin)
admin.site.register(UIMainMenu, UIMainMenuAdmin)
admin.site.register(UISubMenu, UISubMenuAdmin)
