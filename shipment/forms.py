from django import forms
from django.contrib.auth import get_user_model
from shipment.models import UserConfig

User = get_user_model()


class WidgetsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(WidgetsForm, self).__init__(*args, **kwargs)
        self.fields["widget"].required = False

    class Meta:
        model = UserConfig
        fields = ["widget", "user"]
        widgets = {"widget": forms.CheckboxSelectMultiple, "user": forms.HiddenInput()}
