from django.utils.translation import ugettext_lazy as _
from detection.models import Panel
from guardmaster import common as Common
from django.db import models

# Create your models here.


class Server(models.Model):
    SERVER_TYPE_LIST = {
        ('dir', _('Dir Server')),
        ('cdn', _('CDN Server')),
        ('normal', _('Normal Server')),
        ('update', _('Update Server')),
        ('redundance', _('Redundance Update Server')),
        ('world', _('World Server')),
        ('zone', _('Zone Server')),
        ('all', _('GameAll Server')),
    }
    label = models.CharField(max_length=45, unique=True)
    panel = models.ForeignKey(Panel)
    server_type = models.CharField(max_length=45, choices=SERVER_TYPE_LIST)
    ip = models.GenericIPAddressField()
    inetip = models.GenericIPAddressField()
    port = models.IntegerField(help_text=_('GM Port, Usually Is 9135'))
    ssh_port = models.IntegerField(help_text=_('SSH Port, Usually Is 22'))
    hostname = models.CharField(max_length=45)
    home = models.CharField(max_length=60)
    user = models.CharField(max_length=45)
    cdn_url = models.CharField(max_length=256, blank=True, null=True)
    perform = models.CharField(max_length=45)
    world_id = models.IntegerField()
    db_user = models.CharField(max_length=45)
    db_password = models.CharField(max_length=45)
    db_host = models.GenericIPAddressField()
    buf = models.IntegerField()

    def __unicode__(self):
        return self.label

    class Meta:
        db_table = 'config_server'


class ResponseMail(models.Model):
    title = models.CharField(max_length=45)
    content = models.CharField(max_length=256)
    server = models.ForeignKey(Server)
    guardmaster = models.CharField(max_length=45)
    uid = models.IntegerField()
    accessory = models.TextField()
    response_id = models.BigIntegerField()
    pub_date = models.DateTimeField()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']


class ResponseAllMail(models.Model):
    title = models.CharField(max_length=45)
    content = models.CharField(max_length=256)
    server = models.ForeignKey(Server)
    guardmaster = models.CharField(max_length=45)
    version = models.CharField(max_length=45)
    zone = models.CharField(max_length=256)
    accessory = models.TextField()
    status = models.IntegerField()
    response_list = models.CharField(max_length=256)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-id']


class Notify(models.Model):
    panel = models.ForeignKey(Panel)
    title = models.CharField(max_length=256)
    content = models.TextField()
    is_display = models.IntegerField()
    link = models.CharField(max_length=256, blank=True, null=True)
    hostname = models.CharField(max_length=45)
    channel = models.CharField(max_length=256)
    platform = models.CharField(max_length=45)
    world_id = models.CharField(max_length=256)
    version = models.CharField(max_length=128)
    image_width = models.IntegerField()
    image_height = models.IntegerField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    is_title = models.BooleanField(default=True)
    seqid = models.IntegerField()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['seqid', 'hostname', 'channel', 'platform']


class GmOrder(models.Model):
    label = models.CharField(max_length=64)
    param_count = models.IntegerField()
    is_work = models.IntegerField(default=0)
    remarks = models.CharField(max_length=256)
    seqid = models.IntegerField()

    def __unicode__(self):
        return self.label

    class Meta:
        ordering = ['seqid']
