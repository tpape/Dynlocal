from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from Applications.api.models import UserProfile, ProfileContributer
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset, ButtonHolder, MultiField
from django.contrib.auth.forms import AuthenticationForm

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

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email=email).count() > 0:
            raise forms.ValidationError(_("Cette adresse existe déjà"), code='invalid')
        return email
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-register-form'
        self.helper.form_class = 'register-form'
        self.helper.form_method = 'post'
        self.helper.form_action = '/contrib/'
        self.helper.layout = Layout(
            Fieldset(
                'Inscrivez-vous',
                'username',
                'email',
                'password',
                'confirmation',
                ),

            ButtonHolder(
                Submit('submit', 'Submit', css_class='button white')
                )
        )

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        exclude = ('registration_history','user_id','user')

class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-login-form'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = '/contrib/login'
        self.helper.layout = Layout(
            Fieldset(
                'Connectez-vous',
                'username',
                'password',
                ),

          ButtonHolder(
                Submit('submit', 'Submit', css_class='button white')
            )
        )
class ContributerProfileForm(forms.ModelForm):

    class Meta:
        model = ProfileContributer
        exclude =('latitude','longitude','visible')

    def __init__(self, *args, **kwargs):
        super(ContributerProfileForm, self).__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-profile-form'
        self.helper.form_class = 'from-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = '/contrib/profile/add'
        self.helper.layout = Layout(
            Fieldset(
                'Votre profil',
                'label',
                'img',
                'postal_address',
                'description',
                'availibility',
                'contact',
            ),
              ButtonHolder(
                    Submit('submit', 'Submit', css_class='button white')
                )
        )
