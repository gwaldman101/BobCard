from django import forms
import datetime  # for checking renewal date range.

class RequestAccessForm(forms.Form):
    """Form for a librarian to renew books."""
    requested_location =  forms.CharField(help_text="Enter a location")

    requested_time =forms.TimeField(help_text = "Enter amount of time")
    def clean_renewal_date(self):
        data = self.cleaned_data['requested_location']
        
        return data
