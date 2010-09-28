# views.py
#
# Copyright (c) 2010 UK Citizens Online Democracy. All rights reserved.
# Email: francis@mysociety.org; WWW: http://www.mysociety.org/

from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import get_object_or_404

from forms import AlertForm
from models import Alert
from utils import render

def home(request):
    form = AlertForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            alert = form.save()
            send_confirmation_email(request, alert)
            return render(request, 'check-email.html')
    return render(request, 'register.html', { 'form': form })

