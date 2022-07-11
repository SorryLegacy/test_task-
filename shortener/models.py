from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class ShortUrl(models.Model):
    """ """
    url = models.URLField(verbose_name="Normal Url")
    short_url = models.CharField(verbose_name="Short Url", max_length=11, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self): 
        return self.url
