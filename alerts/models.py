import urllib2
import simplejson

from django.contrib.gis.db import models
from django.contrib.contenttypes import generic
from applications.models import Application
from emailconfirmation.models import EmailConfirmation

class Alert(models.Model):
    email = models.EmailField()
    postcode = models.CharField(max_length=8, null=True, blank=True)
    ward_mapit_id = models.IntegerField(null=True, blank=True)
    location = models.PointField(null=True)
    radius = models.IntegerField(
        default=800, 
        null=True,
        blank=True,
        choices=(
            (183, 'about 200 yards / 180m'),
            (800, 'about half a mile / 800m'),
            (1600, 'about a mile / 1.6km'),
            ),
        )
    applications = models.ManyToManyField(Application)
    confirmed = generic.GenericRelation(EmailConfirmation)

    objects = models.GeoManager()

    _ward_name = None

    @property
    def ward_name(self):
        if self.ward_mapit_id and not self._ward_name:
            # Make a dictionary of ward name to id
            mapit_response = urllib2.urlopen("http://mapit.mysociety.org/area/%s" %self.ward_mapit_id)
            mapit_data = simplejson.load(mapit_response)
            self._ward_name = mapit_data.get('name')
        
        return self._ward_name

    class Meta:
        ordering = ('email',)

    def __unicode__(self):
        return 'Alert around %s, radius %s, for %s' % (self.location, self.radius, self.email)

