from django import forms
from .models import Remember


class RememberForm(forms.ModelForm):
    class Meta:
        model = Remember
        fields = [
            "remember",
            "tags",
        ]
