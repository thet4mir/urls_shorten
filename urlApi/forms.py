from django import forms
from .models import Urls


class UrlForm(forms.ModelForm):
    class Meta:
        model = Urls
        fields =('url',)
