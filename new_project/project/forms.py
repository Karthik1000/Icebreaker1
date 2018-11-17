from django import forms
from .models import post,Profile
from django.contrib.auth.models import User
#from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.forms import UserCreationForm


class UserLoginForm(forms.Form):
    username = forms.CharField(label='',widget=forms.TextInput(attrs = {'placeholder':'username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs = {'placeholder':'password'}))

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=False, help_text='Optional.',widget=forms.TextInput(attrs = {'placeholder':'UserName'}))
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.',widget=forms.TextInput(attrs = {'placeholder':'First Name'}))
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.',widget=forms.TextInput(attrs = {'placeholder':'Last Name'}))
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.',widget=forms.TextInput(attrs = {'placeholder':'Email'}))
    password1 = forms.CharField(max_length=30, required=False, help_text='Optional.',widget=forms.PasswordInput(attrs = {'placeholder':'password'}))
    password2 = forms.CharField(max_length=30, required=False, help_text='Optional.',widget=forms.PasswordInput(attrs = {'placeholder':'Confirm password'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('Password did not match')
        return confirm_password

class UserEditForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude =('user',)
