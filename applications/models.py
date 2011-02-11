from django.contrib.gis.db import models

class Application(models.Model):
    council_reference = models.CharField(max_length=50)
    address = models.TextField()
    postcode = models.CharField(max_length=8)
    location = models.PointField(null=True)
    ward_mapit_id = models.IntegerField(null=True) #The integer mapit id. null=True right now to ease the migration.
    description = models.TextField()
    info_url = models.CharField(max_length=1024)
    created = models.DateTimeField(auto_now_add=True)
    received = models.DateField()

    objects = models.GeoManager()

    def __unicode__(self):
        return 'Planning application for %s (ref %s), made %s' % (self.address, self.council_reference, self.received)

