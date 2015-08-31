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

    def __unicode__(self):
        return self.version

    class Meta:
        ordering = ['-id']
