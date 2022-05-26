from django.db import models


class Server(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    ip = models.CharField(max_length=15, null=False, blank=False, unique=True)
    status = models.BooleanField(blank=True, null=True)

    class Meta:
        app_label = 'servers'
        db_table = 'servers'
        verbose_name = 'server'
        verbose_name_plural = 'servers'
