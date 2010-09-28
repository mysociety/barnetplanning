from django import forms
from django.contrib.localflavor.uk.forms import UKPostcodeField

from models import Alert

# Due to a bug in UKPostcodeField, can't override error message. This is 
# fixed in: http://code.djangoproject.com/ticket/12017
# So remove this extra class when we have a recent enough Django.
class MyUKPostcodeField(UKPostcodeField):
    default_error_messages = {
        'invalid': 'We need your complete UK postcode.'
    }

class AlertForm(forms.ModelForm):
    postcode = MyUKPostcodeField(error_messages = {
        'required': 'Please enter your postcode',
    })

    def __init__(self, *args, **kwargs):
        super(AlertForm, self).__init__(*args, **kwargs)
        self.fields['radius'].widget = forms.RadioSelect()

    class Meta:
        model = Alert
        exclude = ('location',)
