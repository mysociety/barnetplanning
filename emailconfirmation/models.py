from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.auth.tokens import default_token_generator
from utils import int_to_base32, send_email

class EmailConfirmationManager(models.Manager):
    def confirm(self, request, object):
        conf = EmailConfirmation(content_object=object)
        conf.send_email(request)

class EmailConfirmation(models.Model):
    confirmed = models.BooleanField(default=False)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    objects = EmailConfirmationManager()

    def __unicode__(self):
        return 'Confirming of %s, %s' % (self.content_object.email, self.confirmed)

    def send_email(self, request):
        send_email(request, "Alert confirmation",
            'emailconfirmation/email.txt',
            {
                'email': self.content_object.email,
                'id': int_to_base32(self.content_object.id),
                'token': default_token_generator.make_token(self.content_object),
            }, email
        )
        self.save()

