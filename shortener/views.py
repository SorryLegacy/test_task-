from django.views.generic import ListView, CreateView, RedirectView
from django.urls import reverse_lazy
import random
import string

from .models import ShortUrl
from .forms import UrlForm


class UrlShotener(CreateView):
    """Class to make short url"""
    model = ShortUrl
    queryset = ShortUrl.objects.all()
    form_class = UrlForm
    template_name = 'index.html'
    success_url = reverse_lazy("profile")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.short_url = ''.join(random.choice(string.ascii_letters)
                                        for x in range(10))
        if self.request.user.is_authenticated:
            self.object.user = self.request.user
        else:
            self.object.user = None
        self.object.save()
        return super(UrlShotener, self).form_valid(form)


class UserUrl(ListView):
    """Class for user profile"""
    model = ShortUrl

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return ShortUrl.objects.filter(user=self.request.user)
        else:

            return ShortUrl.objects.filter(user=None).order_by('-id')


class RedirectUrl(RedirectView):
    """Class for redirect with short url"""

    def get_redirect_url(self, short):
        url = ShortUrl.objects.get(short_url=short)
        return url.url
