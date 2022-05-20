from django import forms
from django.contrib.auth import get_user_model
from shipment.models import UserConfig

User = get_user_model()


class WidgetsForm(forms.ModelForm):
<<<<<<< HEAD
    def __init__(self, *args, **kwargs):
        super(WidgetsForm, self).__init__(*args, **kwargs)
        self.fields["widget"].required = False

    class Meta:
        model = UserConfig
        fields = ["widget", "user"]
        widgets = {"widget": forms.CheckboxSelectMultiple, "user": forms.HiddenInput()}
=======
    class Meta:
        model = UserConfig
        fields = ("widget",)
>>>>>>> ebceb8a7964ab8ab5834263b0e3dc7ad0effe4e7
