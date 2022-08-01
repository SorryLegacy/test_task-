from django.forms import ModelForm

from .models import ShortUrl


class UrlForm(ModelForm):
    """Form for enter url"""
    class Meta:
        model = ShortUrl
        fields = ("url", )
