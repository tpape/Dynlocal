from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from Applications.api.models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirmation = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password','confirmation')

    def clean_confirmation(self):
            password = self.cleaned_data['password']
            confirmation = self.cleaned_data['confirmation']

            if password != confirmation:
                raise forms.ValidationError(_("La confirmation ne correspond pas au mot de passex"), code='invalid')
            return confirmation

class UserProfileForm(forms.ModelForm):

       class Meta:
        model = UserProfile
        exclude = ('registration_history',)
