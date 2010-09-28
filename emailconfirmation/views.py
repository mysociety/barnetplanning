from django.http import Http404
from django.shortcuts import get_object_or_404
from models import EmailConfirmation
from utils import base32_to_int

def check_token(request, id, token):
    try:
        id = base32_to_int(id)
    except ValueError:
        raise Http404

    confirmation = get_object_or_404(EmailConfirmation, id=id)
    if default_token_generator.check_token(confirmation, token):
        confirmation.validated = True
        confirmation.save()
        return render(request, 'registration/validated.html', {
            'user': user,
        })
    return HttpResponseRedirect('/')

