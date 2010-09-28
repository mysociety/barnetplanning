from django.template import loader, Context
from django.core.mail import send_mail
from django.conf import settings

def send_email(request, subject, template, context, to):
    t = loader.get_template(template)
    context.update({
        'host': request.META['HTTP_HOST'],
    })
    mail = t.render(Context(context))
    send_mail(subject, mail, settings.DEFAULT_FROM_EMAIL, [to])

# Miss out i l o u
digits = "0123456789abcdefghjkmnpqrstvwxyz"

class MistypedIDException(Exception):
    pass

def base32_to_int(s):
    """Convert a base 32 string to an integer"""
    mistyped = False
    if s.find('o')>-1 or s.find('i')>-1 or s.find('l')>-1:
        s = s.replace('o', '0').replace('i', '1').replace('l', '1')
        mistyped = True
    decoded = 0
    multi = 1
    while len(s) > 0:
        decoded += multi * digits.index(s[-1:])
        multi = multi * 32
        s = s[:-1]
    if mistyped:
        raise MistypedIDException(decoded)
    return decoded

def int_to_base32(i):
    """Converts an integer to a base32 string"""
    enc = ''
    while i>=32:
        i, mod = divmod(i,32)
        enc = digits[mod] + enc
    enc = digits[i] + enc
    return enc


