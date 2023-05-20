from django import forms
from .models import Ads, Response


class AdForm(forms.ModelForm):
    class Meta:
        model = Ads
        fields = [
            'header',
            'text',
            'category',
        ]


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = [
            'text',
        ]
