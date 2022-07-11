from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.forms import ModelForm

from .models import ShortUrl


User = get_user_model()


class CreationForm(UserCreationForm):
    """"""
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', )


class UrlForm(ModelForm):
    """"""
    class Meta:
        model = ShortUrl
        fields = ("url", )
