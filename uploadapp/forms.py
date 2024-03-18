from django import forms
from django.utils.translation import gettext_lazy as _

from .models import JobApplication, Uploads

class UploadForm(forms.ModelForm):
    class Meta:
        model = Uploads
        fields = "__all__"


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ["first_name", "last_name", "email", "file", "description"]
        labels = {
            "first_name": _("First Name:"),
            "last_name": _("Last Name:"),
            "email": _("Email Address:"),
            "file": _("Upload Resume:"),
            "description": _("Description (Optional):"),
        }