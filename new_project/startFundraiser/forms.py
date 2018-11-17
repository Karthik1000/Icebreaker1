from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import Campaign, FAQs


class DateInput(forms.DateInput):
    input_type = 'date'


class CampaignForm(forms.ModelForm):

    class Meta:
        model = Campaign
        exclude = ['user', 'pledged', 'people_pledged']
        widgets = {
            'start_Date': DateInput(),
            'end_Date': DateInput(),
            'campaign_Title': forms.TextInput(attrs={'required': True, 'placeholder': 'Title'}),
            'campaign_': forms.TextInput(attrs={'required': True}),
            'overview': forms.Textarea(attrs={'cols': 10, 'rows': 10})
        }

        labels = {
            'image': _('Overview Image'),
        }
        help_texts = {
            'overview': _('Tell us about your campaign in a few words.'),
            'story': _('What would you like the supporters to know? '),
            'tags': _('Words that you\'d associate your campaign with.'),
        }
        error_messages = {
            'campaign_Tagline': {
                'max_length': _("This title is too long."),
            },
        }

"""
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
"""
# class BasicsForm(forms.ModelForm):
#
#     class Meta:
#         model = Basics
#         fields = '__all__'
#
#
# class ContentForm(forms.ModelForm):
#
#     class Meta:
#         model = Content
#         fields = '__all__'
#         help_texts = {
#             'overview': _('Tell us about your campaign'),
#         }
#
#
# class FundingForm(forms.ModelForm):
#
#     class Meta:
#         model = Funding
#         fields = ['goal', 'start_Date', 'duration']


class FAQsForm(forms.ModelForm):

    class Meta:
        model = FAQs
        fields = '__all__'
