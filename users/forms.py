from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import CustomUser
from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate, get_user_model, password_validation


class PlaceholderUsernameField(UsernameField):
    
    def widget_attrs(self, widget):
        return {
            **super().widget_attrs(widget),
            "autocapitalize": "none",
            "autocomplete": "username",
            "placeholder": "Username",
        }



class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('user_type', 'username')
        field_classes = {"username": PlaceholderUsernameField}

    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "placeholder": "Password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "placeholder": "Repeat password"}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
