from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserCreationForm as UserCreationFormDjango
)
from django import forms
from django.utils.translation import gettext_lazy

User = get_user_model()


class AjaxAuthenticationForm(forms.Form):
    email = forms.EmailField(
        label=gettext_lazy("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )
    password = forms.CharField(
        label=gettext_lazy("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'})
    )


class UserCreationForm(UserCreationFormDjango):
    email = forms.EmailField(
        label=gettext_lazy("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )

    class Meta(UserCreationFormDjango.Meta):
        model = User
        fields = ("username", "email")
