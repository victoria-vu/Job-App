from django import forms
from django.utils.translation import gettext_lazy as _

from subscribe.models import Subscribe

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = "__all__"
        labels = {
            "first_name": _("First Name:"),
            "last_name": _("Last Name:"),
            "email": _("Email Address:")
        }
        error_messages = {
            "first_name": {
                "required": _("First name is required.")
            },
            "last_name": {
                "required": _("Last name is required.")
            },
            "email": {
                "required": _("An email is required.")
            }
        }