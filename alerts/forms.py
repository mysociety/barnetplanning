import urllib2
import simplejson

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
    widget = forms.TextInput(attrs={'size':'8'})

class AlertForm(forms.ModelForm):
    email = forms.EmailField(label='Your email address', error_messages={'required': 'Please enter your email address.'})
    postcode = MyUKPostcodeField(required=False)
    ward_mapit_id = forms.TypedChoiceField(required=False, coerce=int, initial=None)

    def __init__(self, *args, **kwargs):
        super(AlertForm, self).__init__(*args, **kwargs)
        self.fields['radius'].label = 'If you chose a postcode, how far around your postcode would you like to receive alerts for?'
        # Because radius is not compulsory on the model, choices has puts in a blank row for leaving
        # it out. We don't want that, hence the [1:]
        self.fields['radius'].widget = forms.RadioSelect(choices=self.fields['radius'].choices[1:])

        # Make a dictionary of ward name to id
        mapit_response = urllib2.urlopen("http://mapit.mysociety.org/area/2489/children.json")
        mapit_data = simplejson.load(mapit_response)

        ward_choices = [(int(value), mapit_data[value]['name']) for value in mapit_data]
        ward_choices.sort(key=lambda x: x[1])

        # FIXME - at some point in the future, should work out why None doesn't work here,
        # and get rid of the clean_ward_mapit_id method.
        ward_choices.insert(0, (-1, 'Select'))

        self.fields['ward_mapit_id'].choices = ward_choices
        self.fields['ward_mapit_id'].label = 'Ward'

    def clean_ward_mapit_id(self):
        """We can't use None directly in the form, as it gets stringified into 'None'.
        Instead, we use -1 as the signifier of nothing chosen, and turn it into None here."""
        
        ward_id = self.cleaned_data['ward_mapit_id']

        if ward_id == -1:
            return None
        else:
            return ward_id

    def clean(self):
        cleaned_data = super(AlertForm, self).clean()

        postcode = cleaned_data.get('postcode')
        ward_mapit_id = cleaned_data.get('ward_mapit_id')
        
        if postcode and ward_mapit_id:
            raise forms.ValidationError('Please choose either a postcode or a ward, but not both')
        if not postcode and not ward_mapit_id:
            raise forms.ValidationError('Please enter a postcode or a ward.')

        return cleaned_data

    class Meta:
        model = Alert
        fields = ('postcode', 'ward_mapit_id', 'email', 'radius')
