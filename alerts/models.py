from django.contrib.gis.db import models
from mapit.managers import GeoManager

class Alert(models.Model):
    email = models.EmailField()
    location = models.PointField(null=True)
    radius = models.IntegerField()

    objects = GeoManager()

    class Meta:
        ordering = ('email',)

    def __unicode__(self):
        return 'Alert around %s, radius %s, for %s' % (self.location, self.radius, self.email)

