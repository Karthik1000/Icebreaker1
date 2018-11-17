from django import forms
from .models import *


class Contribute_form(forms.ModelForm):
    class Meta:
        model = Funding
        fields = [
            'name', 'amount', 'email', 'phone_number', 'campaign_Title']
