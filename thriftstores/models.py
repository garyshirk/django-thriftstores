from __future__ import unicode_literals

from django.db import models

class ThriftStore(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    bizID = models.IntegerField()
    bizName = models.CharField(max_length=50)
    bizCat = models.CharField(max_length=50, blank=True, default='')
    bizCatSub = models.CharField(max_length=50, blank=True, default='')
    bizAddr = models.CharField(max_length=100)
    bizCity = models.CharField(max_length=50)
    bizState = models.CharField(max_length=50)
    bizZip = models.CharField(max_length=20)
    bizPhone = models.CharField(max_length=50, blank=True, default='')
    bizEmail = models.CharField(max_length=100, blank=True, default='')
    bizURL = models.CharField(max_length=100, blank=True, default='')
    locLat = models.FloatField(db_index=True)
    locLong = models.FloatField(db_index=True)

    def __unicode__(self):
        return self.bizName

    def __str__(self):
        return self.bizName
