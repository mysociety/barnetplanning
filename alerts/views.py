# views.py
#
# Copyright (c) 2010 UK Citizens Online Democracy. All rights reserved.
# Email: francis@mysociety.org; WWW: http://www.mysociety.org/

from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import get_object_or_404
from django.contrib.gis.geos import Point

from emailconfirmation.models import EmailConfirmation

from forms import AlertForm
from utils import render, postcode_lookup

def home(request):
    form = AlertForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            alert = form.save(commit=False)
            location = postcode_lookup(alert.postcode)
            alert.location = Point(location['wgs84_lon'], location['wgs84_lat'])
            alert.save()
            EmailConfirmation.objects.confirm(
                request, alert,
                'alert-confirmed', 'alert-unsubscribed'
            )
            return render(request, 'check-email.html')
    return render(request, 'home.html', { 'form': form })

def confirmed(request, id):
    return render(request, 'confirmed.html')

def unsubscribed(request, id):
    return render(request, 'unsubscribed.html')
    
