# coding:utf8
from django.utils.translation import ugettext_lazy as _
from detection.models import Panel
from django.db import models


class HostName(models.Model):
    label = models.CharField(max_length=45)
    dir_path = models.CharField(max_length=45)
    panel = models.ForeignKey(Panel)

    def __unicode__(self):
        return self.label


class Platform(models.Model):
    label = models.CharField(max_length=45)
    panel = models.ForeignKey(Panel)

    def __unicode__(self):
        return self.label


class Channel(models.Model):
    label = models.IntegerField()
    panel = models.ForeignKey(Panel)

    def __unicode__(self):
        return str(self.label)


class Ip(models.Model):
    label = models.GenericIPAddressField()
    panel = models.ForeignKey(Panel)

    def __unicode__(self):
        return str(self.label)


class CIWP(models.Model):
    label = models.CharField(max_length=45)
    panel = models.ForeignKey(Panel)

    def __unicode__(self):
        return self.label


class UpLoadWorkOrder(models.Model):
    hostname = models.CharField(max_length=45)
    platform = models.CharField(max_length=45)
    channel = models.IntegerField()
    version = models.CharField(max_length=45)
    progress = models.IntegerField()
    start_date = models.DateTimeField()
    stop_date = models.DateTimeField(blank=True, null=True)
    server = models.CharField(max_length=45)
    user = models.CharField(max_length=45)
    result = models.CharField(max_length=255)
    panel = models.ForeignKey(Panel)
    status = models.IntegerField()
    update_list = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.version

    class Meta:
        ordering = ['-id']


class UpLoadWorkOrderLock(models.Model):
    hostname = models.CharField(max_length=45)
    platform = models.CharField(max_length=45)
    channel = models.IntegerField()
    status = models.IntegerField()
    panel = models.ForeignKey(Panel)

    def __unicode__(self):
        return '{0}/{1}/{2}'.format(self.hostname, self.platform, self.channel)


class TplTemplate(models.Model):
    tpl_type = models.CharField(max_length=45)
    out_file_type = models.CharField(max_length=45)
    out_name_mask = models.CharField(max_length=45)
    out_dir = models.CharField(max_length=45)
    saved_path = models.CharField(max_length=45)

    def __unicode__(self):
        return self.tpl_type

    class Meta:
        db_table = 'tpl_template'


class TplItem(models.Model):
    module_name = models.CharField(max_length=45)
    module_times = models.IntegerField()
    module_seqid = models.IntegerField()
    item_name = models.CharField(max_length=45)
    editable = models.IntegerField()
    item_desc = models.CharField(max_length=255, blank=True, null=True)
    item_default = models.CharField(max_length=255, blank=True, null=True)
    item_valuelist = models.TextField(blank=True, null=True)
    seqid = models.IntegerField()
    tpl_template = models.ForeignKey(TplTemplate)

    def __unicode__(self):
        return '[{0}]{1}'.format(self.module_name, self.item_name)

    class Meta:
        db_table = 'tpl_item'
        ordering = ['seqid', 'module_seqid']


class ServerControlWorkOrder(models.Model):
    server = models.CharField(max_length=45)
    parameter1 = models.CharField(max_length=256, blank=True, null=True)
    parameter2 = models.CharField(max_length=256, blank=True, null=True)
    parameter3 = models.CharField(max_length=256, blank=True, null=True)
    parameter4 = models.CharField(max_length=256, blank=True, null=True)
    parameter5 = models.CharField(max_length=256, blank=True, null=True)
    progress = models.IntegerField()
    start_date = models.DateTimeField()
    stop_date = models.DateTimeField(blank=True, null=True)
    user = models.CharField(max_length=45)
    result = models.CharField(max_length=255)
    panel = models.ForeignKey(Panel)
    status = models.IntegerField()

    def __unicode__(self):
        return self.server

    class Meta:
        ordering = ['-id']


class ServerControlWorkOrderLock(models.Model):
    server = models.CharField(max_length=45)
    status = models.IntegerField()
    panel = models.ForeignKey(Panel)

    def __unicode__(self):
        return self.server


class DataBin(models.Model):
    label = models.CharField(max_length=256)
    panel = models.ForeignKey(Panel)

    def __unicode__(self):
        return self.label


class ProcessServer(models.Model):
    label = models.CharField(max_length=256)
    panel = models.ForeignKey(Panel)

    def __unicode__(self):
        return self.label


class ServerConfigOrder(models.Model):
    label = models.CharField(max_length=45)
    ciwp = models.ForeignKey(CIWP)
    version = models.CharField(max_length=64)
    db_list = models.ManyToManyField(DataBin)
    ps_list = models.ManyToManyField(ProcessServer, related_name='ps_list')
    hs_list = models.ManyToManyField(ProcessServer, related_name='hs_list')
    hs_free_list = models.ManyToManyField(ProcessServer, related_name='hs_free_list')
    db_filename = models.CharField(max_length=256)
    ps_filename = models.CharField(max_length=256)
    hs_filename = models.CharField(max_length=256)
    date = models.DateTimeField()
    user = models.CharField(max_length=45)
    panel = models.ForeignKey(Panel)

    def __unicode__(self):
        return self.label

    class Meta:
        ordering = ['-id', '-date']
