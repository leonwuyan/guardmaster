from django.utils.translation import ugettext_lazy as _
from detection.models import Panel
from guardmaster import common as Common
from django.db import models

# Create your models here.


class Server(models.Model):
    label = models.CharField(max_length=45, unique=True)
    panel = models.ForeignKey(Panel)
    ip = models.GenericIPAddressField()
    port = models.IntegerField()
    hostname = models.CharField(max_length=45)
    home = models.CharField(max_length=60)

    def __unicode__(self):
        return self.label

    class Meta:
        db_table = 'config_server'


class CDNServer(models.Model):
    label = models.CharField(max_length=45, unique=True)
    panel = models.ForeignKey(Panel)
    ip = models.GenericIPAddressField()
    port = models.IntegerField()
    hostname = models.CharField(max_length=45)
    home = models.CharField(max_length=60)
    cdn_url = models.CharField(max_length=256)

    def __unicode__(self):
        return self.label

    class Meta:
        db_table = 'config_cdn_server'


class ResponseMail(models.Model):
    title = models.CharField(max_length=45)
    content = models.CharField(max_length=256)
    server = models.ForeignKey(Server)
    guardmaster = models.CharField(max_length=45)
    uid = models.IntegerField()
    accessory = models.TextField()
    response_id = models.IntegerField()
    pub_date = models.DateTimeField()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']


class Notify(models.Model):
    panel = models.ForeignKey(Panel)
    title = models.CharField(max_length=256)
    content = models.TextField()
    is_display = models.IntegerField()
    link = models.CharField(max_length=256, blank=True, null=True)
    hostname = models.CharField(max_length=45)
    channel = models.IntegerField()
    platform = models.CharField(max_length=45)
    world_id = models.IntegerField()
    notify_url = models.CharField(max_length=256)
    seqid = models.IntegerField()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['hostname', 'channel', 'platform', 'seqid']
