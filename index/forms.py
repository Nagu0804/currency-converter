from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, OCCUPATION_CHOICES, EDUCATION_CHOICES, INTERESTS_CHOICES

from django import forms
from django.contrib.auth.forms import SetPasswordForm, PasswordResetForm
from django.utils.translation import gettext_lazy as _


class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs['placeholder'] = 'Enter new password'
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].label = ''
        
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm new password'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].label = ''


class CustomPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Enter you Email'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].label = ''


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class ProfileForm(forms.ModelForm):
    _form = {'class': 'form-control mt-2'}
    occupation = forms.ChoiceField(choices=OCCUPATION_CHOICES, required=False, widget=forms.Select(attrs=_form))
    education = forms.ChoiceField(choices=EDUCATION_CHOICES, required=False, widget=forms.Select(attrs=_form))
    interests = forms.ChoiceField(choices=INTERESTS_CHOICES, required=False, widget=forms.Select(attrs=_form))

    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio', 'occupation', 'education', 'interests']
    
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['bio'].widget.attrs.update({'class': 'form-control shadow', 'style': 'overflow:hidden;', 'placeholder': 'Bio', 'rows': 5, 'cols': 20})
        self.fields['bio'].label = ''

        self.fields['profile_picture'].widget = forms.FileInput(attrs={'class': 'form-control-file mt-5', 'accept': 'image/*', 'type': 'file'})
        self.fields['profile_picture'].label = ''