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

    class Meta:
        ordering = ['label']


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
    output = models.TextField()

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


class ProcessServer(models.Model):
    label = models.CharField(max_length=256)
    panel = models.ForeignKey(Panel)

    def __unicode__(self):
        return self.label


class ServerConfigOrder(models.Model):
    ciwp = models.ForeignKey(CIWP)
    version = models.CharField(max_length=64)
    db_list = models.TextField()
    ps_list = models.CharField(max_length=256)
    hs_list = models.CharField(max_length=256)
    hs_free_list = models.CharField(max_length=256)
    db_filename = models.CharField(max_length=256)
    ps_filename = models.CharField(max_length=256)
    hs_filename = models.CharField(max_length=256)
    date = models.DateTimeField()
    user = models.CharField(max_length=45)
    panel = models.ForeignKey(Panel)

    def __unicode__(self):
        return str(self.id)

    class Meta:
        ordering = ['-id']
