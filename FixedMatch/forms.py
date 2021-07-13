from django_countries import fields
from FixedMatch.models import Comment
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django_countries.fields import CountryField


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, max_length=254)
    phone = forms.CharField(required=True, max_length=13)
    first_name = forms.CharField(required=True, max_length=50)
    last_name = forms.CharField(required=True, max_length=50)
    country = CountryField(multiple=False)

    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone',
            'country',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.phone = self.cleaned_data['phone']
        user.email = self.cleaned_data['email']
        # user.first_name = self.cleaned_data['first_name']
        # user.last_name = self.cleaned_data['last_name']
        # user.country = self.cleaned_data['country']

        if commit:
            user.save()

        return user


class CodeForm(forms.Form):
    payment_code = forms.CharField(required=True, max_length=100)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'comment')
