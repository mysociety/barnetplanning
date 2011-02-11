from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^$', 'alerts.views.home'),
    url(r'^confirmed/(\d+)$', 'alerts.views.confirmed', name='alert-confirmed'),
    url(r'^unsubscribed/(\d+)$', 'alerts.views.unsubscribed', name='alert-unsubscribed'),
    (r'^', include('emailconfirmation.urls')),
)
