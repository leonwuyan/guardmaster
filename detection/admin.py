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
        'get_main_menu_id',
        'main_menu',
        'url',
        'table_name',
        'category',
        'seqid')
    search_fields = ['label']
    list_filter = ['category']

    def get_main_menu_id(self, obj):
        m = obj.main_menu
        if m:
            return obj.main_menu.id
        else:
            return 'None'


class UIMainMenuAdmin(admin.ModelAdmin):
    inlines = [UISubMenuInline]
    list_display = ('label', 'group_list', 'panels_list', 'seqid')
    search_fields = ['label']
    list_filter = ['group', 'panels']

    def panels_list(self, obj):
        panels = ""
        for panel in obj.panels.all():
            panels += panel.label + ' | '
        return panels

    def group_list(self, obj):
        groups = ""
        for g in obj.group.all():
            groups += g.name + ' | '
        return groups


class PanelAdmin(admin.ModelAdmin):
    list_display = ('label', 'groups_list', 'db_aliases', 'symbol', 'start_date')
    search_fields = ['label']
    list_filter = ['groups']

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
