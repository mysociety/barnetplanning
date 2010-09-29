from django.contrib.gis.db import models
from applications.models import Application

class Alert(models.Model):
    email = models.EmailField()
    postcode = models.CharField(max_length=8)
    location = models.PointField(null=True)
    radius = models.IntegerField(default=800, choices=(
        (183, 'about 200 yards / 180m'),
        (800, 'about half a mile / 800m'),
        (1600, 'about a mile / 1.6km'),
    ))
    applications = models.ManyToManyField(Application)

    objects = models.GeoManager()

    class Meta:
        ordering = ('email',)

    def __unicode__(self):
        return 'Alert around %s, radius %s, for %s' % (self.location, self.radius, self.email)

