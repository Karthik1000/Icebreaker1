from django import forms
from . import models

class createcomment(forms.ModelForm):
    class Meta:
        model = models.comment
        fields = ['content']
