from crispy_bootstrap5.bootstrap5 import FloatingField
from crispy_forms.bootstrap import InlineField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm as DjangoAuthenticationForm,
    UserCreationForm as DjangoUserCreationForm,
)
from django.utils.translation import gettext_lazy as _

from medux.common.bootstrap import Card
from medux.common.models import User


class AuthenticationForm(DjangoAuthenticationForm):

    remember_me = forms.BooleanField(
        label=_("Remember me"), widget=forms.CheckboxInput(), required=False
    )

    class Meta:
        model = User
        fields = ("username", "password")

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].help_text = ""
        self.fields["username"].widget.attrs.update({"autofocus": True})
        self.fields["password"].help_text = ""

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Card(
                FloatingField("username"),
                FloatingField("password"),
                InlineField("remember_me"),
                title=_("Please sign in to get access to your site."),
            ),
            ButtonHolder(Submit("submit", _("Sign in"), css_class="w-100 btn-lg")),
        )


class SignUpForm(DjangoUserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Username", "class": "form-control"}
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Email", "class": "form-control"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "class": "form-control"}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password check", "class": "form-control"}
        )
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
