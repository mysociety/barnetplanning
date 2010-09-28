import random, hmac, hashlib
from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from utils import int_to_base32, base32_to_int, send_email

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
                'token': self.make_token(random.randint(0,32767)),
            }, email
        )
        self.save()
        return self._make_token_with_timestamp(user, self._num_days(self._today()))

    def check_token(self, token):
        try:
            rand, hash = token.split("-")
        except:
            return False

        try:
            rand = base32_to_int(rand)
        except:
            return False

        if self.make_token(rand) != token:
            return False

        return True

    def make_token(self, rand):
        rand = int_to_base32(rand)
        hash = hmac.new(settings.SECRET_KEY, unicode(self.id) + rand, hashlib.sha1).hexdigest()[::2]
        return "%s-%s" % (rand, hash)
