from django.contrib.gis.db import models

class Alert(models.Model):
    email = models.EmailField()
    postcode = models.CharField(max_length=8)
    location = models.PointField(null=True)
    radius = models.IntegerField()

    objects = models.GeoManager()

    class Meta:
        ordering = ('email',)

    def __unicode__(self):
        return 'Alert around %s, radius %s, for %s' % (self.location, self.radius, self.email)

