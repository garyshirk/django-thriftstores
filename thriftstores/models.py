from __future__ import unicode_literals

from django.db import models

class ThriftStore(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    storeid = models.CharField(max_length=50)
    categorymain = models.CharField(max_length=50, blank=True, default='')
    categorysub = models.CharField(max_length=50, blank=True, default='')
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)
    phone = models.CharField(max_length=50, blank=True, default='')
    email = models.CharField(max_length=100, blank=True, default='')
    website = models.CharField(max_length=100, blank=True, default='')
    loclat = models.DecimalField(max_digits=9,decimal_places=6)
    loclong = models.DecimalField(max_digits=9,decimal_places=6)

    class Meta:
        ordering = ('created',)

"""--------------------------------------------------------------------
    Basic floating-point storage for GPS lat/lng coords.
    
    Abstract base clase so it can be customized as needed on implementation.
--------------------------------------------------------------------"""
class GPSPosition(models.Model):
    latitude = models.FloatField(blank=False, db_index=True)
    longitude = models.FloatField(blank=False, db_index=True)
    gps_position_display_name = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        abstract = True


"""--------------------------------------------------------------------
    A GPSPosition with a specified radius and corresponding area
    bounding box.
    
    Assumes a square bounding box -- which is not true as longitude
    converges at the poles.

    https://github.com/kdmukai/gps_position/blob/master/gps_position/models.py
--------------------------------------------------------------------"""
class GPSArea(GPSPosition):
    radius = models.FloatField(blank=True, null=True)
    max_lat = models.FloatField(blank=True, null=True, db_index=True)
    min_lat = models.FloatField(blank=True, null=True, db_index=True)
    max_lng = models.FloatField(blank=True, null=True, db_index=True)
    min_lng = models.FloatField(blank=True, null=True, db_index=True)
    
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        import math
        if self.radius:
            # Calculate the max/min coords
            
            # Circumference of the Earth from pole-to-pole: 40,007km
            # 360degrees/40007km = 0.0089984253 degrees latitude/km
            lat_km = 0.0089984253
            
            # Circumference of the Earth @ equator: 40,075km
            # 360degrees/cos(lat)/40075km = x degrees longitude/km @ latitude
            lng_km = 0.0089831566 / math.cos(math.radians(self.latitude))
            
            # Calculate the bounding box defined by the radius
            self.max_lat = self.latitude + lat_km*self.radius
            self.min_lat = self.latitude - lat_km*self.radius
            self.max_lng = self.longitude + lng_km*self.radius
            self.min_lng = self.longitude - lng_km*self.radius
            
        super(GPSArea, self).save(*args, **kwargs) # Call the "real" save() method.


    def contains(self, gps_position):
        if (self.min_lat <= gps_position.latitude and
            self.max_lat >= gps_position.latitude and
            self.min_lng <= gps_position.longitude and
            self.max_lng >= gps_position.longitude):
            return True
        else:
            return False

    
