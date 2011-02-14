# views.py
#
# Copyright (c) 2010 UK Citizens Online Democracy. All rights reserved.
# Email: francis@mysociety.org; WWW: http://www.mysociety.org/

from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import get_object_or_404
from django.contrib.gis.geos import Point

from emailconfirmation.models import EmailConfirmation
from static_texts.models import StaticText

from forms import AlertForm
from utils import render, postcode_lookup

def home(request):
    form = AlertForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            alert = form.save(commit=False)
            if alert.postcode:
                location = postcode_lookup(alert.postcode)
                alert.location = Point(location['wgs84_lon'], location['wgs84_lat'])
            else:
                alert.radius = None
            alert.save()
            EmailConfirmation.objects.confirm(
                request, alert,
                'alert-confirmed', 'alert-unsubscribed'
            )

            text = StaticText.objects.get(place='check-email').text
            return render(request, 'check-email.html', { 'text': text })

    return render(request, 'home.html', { 'form': form })

def confirmed(request, id):
    text = StaticText.objects.get(place='confirmed').text
    return render(request, 'confirmed.html', { 'text': text })

def unsubscribed(request, id):
    text = StaticText.objects.get(place='unsubscribed').text
    return render(request, 'unsubscribed.html', { 'text': text })
    
