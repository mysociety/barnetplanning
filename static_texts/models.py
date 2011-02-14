from django.db import models

PLACE_CHOICES = (
    ('confirmed', 'Web page after confirmation link clicked'),
    ('unsubscribed', 'Web page after unsubscribe link clicked'),
    ('check-email', 'Web page after form submitted, asking user to check their email'),
#    ('email-confirm', 'Email sent containing alert confirmation link'),
    ('email-alert', 'Email sent containing a new planning alert (footer)'),
)

# Create your models here.
class StaticText(models.Model):
    place = models.CharField(editable=False, unique=True, max_length=20, choices=PLACE_CHOICES)
    text = models.TextField(blank=True)

    def __unicode__(self):
        return self.get_place_display()
