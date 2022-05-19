from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    is_supplier = forms.BooleanField(label="Are You Supplier", required=False)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "is_supplier",
            "is_customer",
            "password1",
            "password2",
        ]
        widgets = {"is_customer": forms.HiddenInput()}
