from django import forms
from .models import Remember
from martor.fields import MartorFormField


class RememberForm(forms.ModelForm):
    class Meta:
        model = Remember
        fields = [
            "remember",
            "tags",
        ]
