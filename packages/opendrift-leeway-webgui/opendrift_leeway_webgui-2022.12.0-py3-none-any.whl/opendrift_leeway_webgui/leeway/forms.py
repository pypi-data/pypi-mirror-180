"""
Forms for the web GUI
"""
from django.forms import ModelForm, CharField, TextInput

from .models import LeewaySimulation
from .utils import normalize_dms2dec

class LeewaySimulationForm(ModelForm):
    """
    Add a form for simulations with some tweaks of the default.
    """
    def __init__(self, *args, **kwargs):
        """
        Use CharField for latitude and longitude to allow DMS input
        """
        super().__init__(*args, **kwargs)
        self.fields['longitude'] = CharField(
            help_text='(E/W) Input in decimal and degrees minutes seconds supported.',
            widget=TextInput(attrs={'placeholder':'12° 26\' 42.684"'}))
        self.fields['latitude'] = CharField(
            help_text='(N/S) Input in decimal and degrees minutes seconds supported.',
            widget=TextInput(attrs={'placeholder':'34° 47\' 49.1166"'}))

    class Meta:  # pylint: disable=too-few-public-methods
        """
        Configure form fields and help text.
        """
        model = LeewaySimulation
        fields = ['latitude', 'longitude', 'object_type', 'start_time', 'duration', 'radius']

        help_texts = {
            'duration': 'Length of simulation in hours.',
            'radius': ('Radius for distributing drifting particles around '
                       'the start coordinates in meters.')
        }

    def clean_longitude(self):
        """
        Convert longitude DMS to decimal
        """
        return normalize_dms2dec(self.cleaned_data.get('longitude', ''))

    def clean_latitude(self):
        """
        Convert latitude DMS to decimal
        """
        return normalize_dms2dec(self.cleaned_data.get('latitude', ''))
