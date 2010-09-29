from django import forms
from django.contrib.localflavor.uk.forms import UKPostcodeField

from models import Alert

# Due to a bug in UKPostcodeField, can't override error message. This is 
# fixed in: http://code.djangoproject.com/ticket/12017
# So remove this extra class when we have a recent enough Django.
class MyUKPostcodeField(UKPostcodeField):
    default_error_messages = {
        'required': 'Please enter your postcode',
        'invalid': 'We need your complete UK postcode.'
    }
    widget = forms.TextInput(attrs={'size':'8'})

class AlertForm(forms.ModelForm):
    email = forms.EmailField(label='Your email address', error_messages={'required': 'Please enter your email address.'})
    postcode = MyUKPostcodeField()

    def __init__(self, *args, **kwargs):
        super(AlertForm, self).__init__(*args, **kwargs)
        self.fields['radius'].label = 'How far around your postcode would you like to receive alerts for?'
        self.fields['radius'].widget = forms.RadioSelect(choices=self.fields['radius'].choices)

    class Meta:
        model = Alert
        fields = ('postcode', 'email', 'radius')
