from django import forms
from django.contrib.auth import get_user_model
from shipment.models import UserConfig

User = get_user_model()


class WidgetsForm(forms.ModelForm):
    class Meta:
        model = UserConfig
        fields = ("widget",)
