from django import forms
from django.contrib.auth.forms import (UserCreationForm)
from .models import (GlobUser, UserProfile)


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = GlobUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class EditUserForm(forms.ModelForm):
    class Meta:
        model = GlobUser
        fields = (
            'first_name',
            'last_name',
            'email'
        )


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('description',
                  'city',
                  'country',
                  'website',
                  'phone',
                  'type',
                  'image')



